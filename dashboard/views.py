from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from api.models import Warehouse, Organization, Client, Order, CustomUser, OrderDetail, Todo, VisitingImages, \
    OrderProductRows, Aksiya
from product.models import Product, ProductSeria, ProductBrand
from authentic.integrations import client, GetDailyReport, werehouse, product_sales
from .datasync import Orders_sync, Clients_sync, Organizations_sync, Werehouse_sync, OrderDetails_sync, \
    GetProductsBlance_sync
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .statistics import daily_order_statistics, most_sold_products_monthly_by_user, product_sales_statistics_by_user, \
    yearly_sales_statistics_by_user, most_purchased_product_by_user_clients, clients_monthly_trade_by_user, \
    popular_categories_monthly_by_user, daily_order_statistics_for_month, monthly_trade_for_year, \
    monthly_product_sales_statistics, six_month_product_sales_statistics, six_month_product_sales_statistics2
from product.serializers import ProductSerializer
from django.db.models import Sum, Count, Max, Min, Q, Avg

from .utils import get_business_regions, calculate_active_clients, calculate_passive_clients, group_clients_by_orders


# IndexView displays the index page and handles user authentication
class IndexView(LoginRequiredMixin, View):
    """
    IndexView displays the index page and handles user authentication.

    Methods:
        get(request): Handles GET requests and renders the index page.
    """
    # Specifies the login page URL if the user is not logged in
    login_url = reverse_lazy('authentic:login')

    # Handles GET request for the index page
    def get(self, request):
        """
        Handles GET request for the index page.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Rendered HTML page with context data.
        """
        today = datetime.today()
        month_first_day = datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        code = request.user.code
        d = {}
        if code:
            kpi = client.service.GetKPI(code)
            report = client.service.GetDailyReport(code)
            d['kpi'] = kpi
            d['report'] = report
            d['aksiya'] = Aksiya.objects.filter(end_date__gte=today)
            return render(request, 'index.html', context=d)
        return render(request, 'index.html', {'message': 'Please connect your 1C account'})


# statistic_data collects statistics related to user orders
def statistic_data(user, ):
    """
    Collects statistics related to user orders within the current month.

    Args:
        user (User): The user for whom the statistics are being calculated.

    Returns:
        dict: A dictionary containing statistics data.
    """
    d = {}
    today = datetime.today()
    month_first_day = datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    orders = Order.objects.filter(agent=user, dateOrder__gte=month_first_day, dateOrder__lte=today)
    daily_orders = orders.filter(dateOrder__lte=today).annotate(total_sum=Sum('total'))
    d['orders_count'] = len(orders)
    return d


# EcommerceView provides data for the ecommerce dashboard
class EcommerceView(LoginRequiredMixin, View):
    """
    EcommerceView provides data for the e-commerce dashboard.

    Methods:
        get(request): Renders the e-commerce page with statistics.
        post(request): Handles POST requests for e-commerce actions.
    """
    # Specifies the login page URL if the user is not logged in
    login_url = reverse_lazy('dashboard:login')

    # Handles GET request to render the ecommerce page with statistics
    def get(self, request):
        """
        Handles GET request to render the e-commerce page with statistics.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Rendered e-commerce HTML page with context data.
        """
        code = request.user.code
        if not code:  # Agar agent "code"ga ega bo'lmasa
            return render(request, 'ecommerce.html', context={'message': 'Sizning profilingizda "code" mavjud emas'})

        # Ma'lumotlarni yig'ish
        today = datetime.today()
        d = {
            'business_reg': get_business_regions(code),
            'price_list': client.service.GetPriceTypes(code),
            'sklad': client.service.GetWarehousesUser(code),
            'clients': client.service.GetClients(code),
            'clients_count': len(client.service.GetClients(code)),
            'statistics': statistic_data(request.user),
            'kpi': client.service.GetKPI(code),
            'report': client.service.GetDailyReport(code),
        }

        # Top sotilgan mahsulotlar
        product_selling = OrderProductRows.objects.filter(order__agent=request.user).order_by('-order')[:10]
        d['top_selling_products'] = product_selling.values(
            'id', 'NameProduct', 'CodeProduct', 'Price', 'Amount', 'Total'
        ).annotate(Count('CodeProduct'), Sum('Amount'), Sum('Total'))

        # So'nggi mijozlar
        business_regions = d['business_reg']
        region_codes = [region['Code'] for region in business_regions]
        if business_regions:
            d['recently_clients'] = Client.objects.filter(
                codeRegion=business_regions[0]['Code']
            ).order_by('-created_at')[:5]

        # Faol/passiv mijozlarni aniqlash
        one_month_ago = today - timedelta(days=30)
        one_year_ago = today - timedelta(days=365)
        active_clients = calculate_active_clients(request.user, one_year_ago)
        passive_clients = calculate_passive_clients(request.user, one_month_ago, active_clients, region_codes)
        # O'rtacha va yuqori mijozlar statistikasi
        client_order_counts = group_clients_by_orders(request.user)
        average_orders = client_order_counts.get('average_orders', 0)

        d.update({
            'active_clients': len(active_clients),
            'passive_clients': len(passive_clients),
            'top_clients': client_order_counts.get('top_clients', []),
            'few_clients': client_order_counts.get('few_clients', []),
        })

        return render(request, 'ecommerce.html', context=d)

    # Handles POST request for ecommerce actions
    def post(self, request):
        """
        Handles POST request for e-commerce actions.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            None
        """
        print(request)


# GetStatistics API view fetches and returns user-related statistics
class GetStatistics(APIView):
    """
    GetStatistics API view fetches and returns user-related statistics.

    Methods:
        get(request, *args, **kwargs): Fetches statistics data for the user.
    """
    # Ensures only authenticated users can access this view
    permission_classes = [IsAuthenticated]

    # Handles GET request to provide statistics data
    def get(self, request, *args, **kwargs):
        """
        Fetches statistics for the authenticated user.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: JSON response containing statistics data.
        """
        user = request.user
        year = datetime.today().year
        month = datetime.today().month
        stats = {
            "six_month_product_sales_statistics2": six_month_product_sales_statistics2(user, year, month),
            "six_month_product_sales_statistics": six_month_product_sales_statistics(user),
            "monthly_product_sales_statistics": monthly_product_sales_statistics(user, year),
            "monthly_trade_for_year": monthly_trade_for_year(user, year),
            "daily_order_statistics_for_month": daily_order_statistics_for_month(user, year, month),

            "daily_stats": daily_order_statistics(user),
            "monthly_top_products": most_sold_products_monthly_by_user(user),
            "product_sales": product_sales_statistics_by_user(user),
            "yearly_stats": yearly_sales_statistics_by_user(user),
            "most_purchased_product_by_user_clients": most_purchased_product_by_user_clients(user),
            "clients_monthly_trade_by_user": clients_monthly_trade_by_user(user),
            "popular_categories_monthly_by_user": popular_categories_monthly_by_user(user),
        }

        return Response(stats, status=200)


# CalendarView renders the calendar page for logged-in users
class CalendarView(LoginRequiredMixin, generic.ListView):
    """
    CalendarView renders the calendar page for logged-in users.

    Attributes:
        model (Model): Specifies the User model for the view.
        template_name (str): Path to the calendar template.
        login_url (str): URL to redirect to if the user is not logged in.
    """
    # Specifies the User model for context
    model = User
    template_name = 'calendar.html'
    login_url = reverse_lazy('dashboard:login')


# ChatView renders the chat interface for logged-in users
class ChatView(LoginRequiredMixin, generic.ListView):
    """
    ChatView renders the chat interface for logged-in users.

    Attributes:
        model (Model): Specifies the User model for the view.
        template_name (str): Path to the chat template.
        login_url (str): URL to redirect to if the user is not logged in.
    """
    # Specifies the User model for the chat user context
    model = User
    template_name = 'chat.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


# TodoView handles tasks related to user to-do items
class TodoView(LoginRequiredMixin, View):
    """
    TodoView handles tasks related to user to-do items.

    Methods:
        get(request): Displays all to-do items for the user.
    """
    # Specifies the login page URL if the user is not logged in
    login_url = reverse_lazy('dashboard:login')

    # Handles GET request to display all to-do items for the user
    def get(self, request):
        """
        Handles GET request to display all to-do items for the user.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Rendered to-do HTML page with context data.
        """
        d = {}
        todos = Todo.objects.filter(author=request.user)
        d['todos'] = todos

        return render(request, 'todo.html', context=d)


# EmailListView renders the email inbox view for logged-in users
class EmailListView(LoginRequiredMixin, generic.ListView):
    """
    EmailListView renders the email inbox view for logged-in users.

    Attributes:
        model (Model): Specifies the User model for the view.
        template_name (str): Path to the email inbox template.
        login_url (str): URL to redirect to if the user is not logged in.
    """
    # Specifies the User model for context
    model = User
    template_name = 'email-inbox.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


# EmailReadView renders the email read page for a specific email
class EmailReadView(LoginRequiredMixin, generic.ListView):
    """
    EmailReadView renders the email read page for a specific email.

    Attributes:
        model (Model): Specifies the User model for the view.
        template_name (str): Path to the email read template.
        login_url (str): URL to redirect to if the user is not logged in.
    """
    # Specifies the User model for context
    model = User
    template_name = 'email-read.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


# ProfileView displays the user profile and related data
class ProfileView(LoginRequiredMixin, generic.ListView):
    """
    ProfileView displays the user profile and related data.

    Methods:
        get(request): Retrieves and displays the user's profile data.
    """
    # Specifies the User model for context
    model = User
    template_name = 'profile.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')

    # Handles GET request to retrieve and display user's profile data
    def get(self, request):
        code = request.user.code
        d = {}
        # print(client.service.GetProductBalance())
        today = datetime.today()
        gps_date = today.strftime('%Y%m%d%H%M%S')
        print(gps_date)
        d['business_reg'] = client.service.GetBusinessRegions(code)
        print(d['business_reg'][0])
        d['price_list'] = client.service.GetPriceTypes(code)
        d['sklad'] = client.service.GetWarehousesUser(code)
        gps = client.service.GetGPS(code, gps_date)  # '20240921110122'
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 6)
        pagination = Paginator(gps, per_page)
        page_obj = pagination.get_page(page_number)
        d['gps'] = page_obj
        d['per_page'] = per_page
        recently_clients = Client.objects.filter(codeRegion=d['business_reg'][0]['Code']).order_by('-created_at')[:5]
        # Har bir mijoz uchun buyurtmalarni hisoblash
        today = datetime.today()
        first_day_of_month = today.replace(day=1)
        client_order_counts = Order.objects.filter(agent=request.user, dateOrder__gte=first_day_of_month,
                                                   dateOrder__lte=today).values('clientCode',
                                                                                'clientName').annotate(
            order_count=Count('id')
        )
        client_order_sum = Order.objects.filter(agent=request.user).values('clientCode', 'clientName').annotate(
            order_sum=Sum('total')).order_by('-order_sum')
        print(client_order_sum)
        average_sum = client_order_sum.aggregate(avg_sum=Avg('order_sum'))['avg_sum']
        print(average_sum)
        # O'rtacha buyurtmalar sonini hisoblash
        average_orders = client_order_counts.aggregate(avg_orders=Avg('order_count'))['avg_orders']
        if average_orders is None:
            average_orders = 0  # Agar buyurtmalar bo'lmasa, 0 ga o'rnatamiz

        # Active va passive mijozlarni ajratish
        active_clients = client_order_counts.filter(order_count__gt=average_orders)
        passive_clients = client_order_counts.filter(order_count__lte=average_orders)
        max_order_count = client_order_counts.aggregate(Max('order_count'))['order_count__max']
        # Natijalarni hisoblash
        d['active_clients'] = active_clients.order_by('-order_count')[:5]
        d['passive_clients'] = passive_clients.order_by('order_count')[:5]
        d['recently_clients'] = recently_clients
        d['gallery_images'] = VisitingImages.objects.filter(author=request.user)[:5]
        return render(request, 'profile.html', context=d)


# UserListView retrieves and displays the list of clients for the user
class UserListView(LoginRequiredMixin, View):
    # Specifies the login page URL if the user is not logged in
    login_url = reverse_lazy('dashboard:login')

    # Handles GET request to fetch and render the client list
    def get(self, request):
        d = {}
        # Cilentlar ro'yxatini olish
        clientlist = client.service.GetClients(request.user.code)
        # Qidiruv so'rovi
        search_query = request.GET.get('search', '').strip()

        # Qidiruv logikasi
        if search_query:
            clientlist = [
                client for client in clientlist
                if (search_query.lower() in client['Name'].lower()
                    or search_query.lower() in str(client['Code']).lower()
                    or search_query.lower() in str(client['INN']).lower()
                    or search_query.lower() in str(client['Signboard']).lower()
                    or search_query.lower() in str(client['AdressDelivery']).lower()
                    or search_query.lower() in str(client['CodeRegion']).lower()
                    or search_query.lower() in str(client['ContactPersonPhone']).lower()
                    or search_query.lower() in str(client['ContactPerson']).lower()
                    or search_query.lower() in str(client['ResponsiblePersonPhone']).lower())
            ]

        # Pagination sozlamalari
        per_page = int(request.GET.get('per_page', 10))
        paginator = Paginator(clientlist, per_page)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        # Kontekst ma'lumotlarini qo'shish
        d['per_page'] = per_page
        d['clients'] = page_obj
        d['search_query'] = search_query  # Qidiruv so'rovini shablonda ko'rsatish

        return render(request, 'user-list.html', context=d)


# ClientProfileView displays the profile of a specific client
class ClientProfileView(LoginRequiredMixin, View):
    # Specifies the login page URL if the user is not logged in
    login_url = reverse_lazy('dashboard:login')

    def get(self, request, pk):
        pass


# ProductListView displays a list of products and handles search functionality
class ProductListView(LoginRequiredMixin, generic.ListView):
    # Specifies the User model for context
    model = User
    template_name = 'product-list.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')

    # Handles GET request to retrieve and display product list with filters
    def get(self, request):
        # Initialize context
        d = {}

        # Get user's project and sklad codes
        codeSklad = request.user.codeSklad.code
        codeProject = request.user.codeProject.code

        # Get the list of products
        products = GetProductsBlance_sync(code_project=codeProject, code_sklad=codeSklad)

        # Apply search and filter logic
        search_query = request.GET.get('search', '')
        if search_query:
            # Filter products by search query
            products = [
                product for product in products
                if search_query.lower() in product['name'].lower()
            ]

        # Add filtered products to context
        d['products'] = products
        return render(request, 'product-list.html', context=d)

    def post(self, request):
        # Initialize context
        d = {}

        # Get user's sklad code and update products
        code_sklad = request.user.code_sklad
        GetProductsBlance_sync(code_sklad=code_sklad)

        return render(request, 'product-list.html', context=d)


class ProductView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentic:login')

    def get(self, request):
        d = {}
        products = Product.objects.all()
        d['products'] = products
        brands = ProductBrand.objects.all()
        d['brands'] = brands
        series = ProductSeria.objects.all()
        d['series'] = series
        products = Product.objects.all()

        search_query = request.GET.get('search', '').strip()
        if search_query:
            # Filter products where the name, description, or other fields match the query
            products = products.filter(
                Q(article__icontains=search_query) |
                Q(name_manufacturer__icontains=search_query) |
                Q(working_title__icontains=search_query) |
                Q(brand__name__icontains=search_query)
            )

        # d['products'] = products
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 20)
        d['per_page'] = per_page
        paginator = Paginator(products, per_page)
        try:
            page_obj = paginator.get_page(page_number)  # Get the current page
        except Exception as e:
            page_obj = paginator.get_page(1)  # If an invalid page is requested, fallback to the first page

            # Add paginated products to the context
        d['products'] = page_obj
        d['search_query'] = search_query
        return render(request, 'product.html', context=d)


class ProductDetailView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        d = {}
        product_data = Product.objects.filter(id=product_id).first
        d['product'] = product_data
        return render(request, 'product-detail.html', context=d)


class ErrorPageView(generic.ListView):
    model = User
    template_name = 'error-page.html'
    context_object_name = 'users'


class InvoiceView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'invoice.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


class OrderHistoryView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'order-history.html'
    context_object_name = 'users'

    def get(self, request):
        d = {}
        orderList = client.service.GetOrderList(request.user.code)
        d['orders'] = orderList
        print(orderList)
        return render(request, 'order-history.html', context=d)


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'order-detail.html'
    login_url = reverse_lazy('dashboard:login')

    def get(self, request, order_id):
        date = request.GET.get('date')
        d = {}
        order_detail = client.service.GetOrderDetails(order_id, date, date)
        sklad = Warehouse.objects.filter(code=order_detail['CodeSklad']).first()
        d['order_detail'] = order_detail
        d['sklad'] = sklad
        return render(request, 'order-detail.html', context=d)


class RefreshView(LoginRequiredMixin, View):
    login_url = reverse_lazy('dashboard:login')

    def get(self, request, *args, **kwargs):
        # Fetch warehouse data from the client service
        # Werehouse_sync()
        # Organizations_sync()
        # print(client.service.GetProductBalance('00000000004', '00000000201'))
        c = Clients_sync(request.user.code)
        o1 = Orders_sync(request.user.code)
        od = OrderDetails_sync(request.user.code)
        print(c, o1, od)
        return redirect('dashboard:index')


class SearchFilterViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('code_sklad',)
    search_fields = ('name',)
