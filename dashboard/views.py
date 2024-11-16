from django.db.models import Count, Sum, Max, Min
from django.contrib.auth.models import User
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout

from api.models import Warehouse, Organization, Client, Order, CustomUser, OrderDetail, Todo, VisitingImages, \
    OrderProductRows
from product.models import Product, ProductSeria, ProductBrand
from authentic.integrations import client, GetDailyReport, werehouse, product_sales
from .datasync import Orders_sync, Clients_sync, Organizations_sync, Werehouse_sync, OrderDetails_sync, \
    GetProductsBlance_sync


class IndexView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentic:login')

    def get(self, request):
        code = request.user.code
        d = {}
        if code:
            kpi = client.service.GetKPI(code)
            report = client.service.GetDailyReport(code)
            d['kpi'] = kpi
            d['report'] = report
            return render(request, 'index.html', context=d)
        return render(request, 'index.html', {'message': 'Please connect your 1C account'})


class EcommerceView(LoginRequiredMixin, View):
    login_url = reverse_lazy('dashboard:login')

    def get(self, request):
        d = {}
        productSelling = OrderProductRows.objects.filter(order__agent=request.user).order_by('-order')[:10]
        topSellingProducts = productSelling.values('NameProduct', 'CodeProduct', 'Price', 'Amount', 'Total').annotate(
            Count('CodeProduct'),
            Sum('Amount'), Sum('Total'))
        d['topSellingProducts'] = topSellingProducts[:5]
        print(d['topSellingProducts'])
        d['productSelling'] = productSelling
        return render(request, 'ecommerce.html', context=d)


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'calendar.html'
    login_url = reverse_lazy('dashboard:login')


class ChatView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'chat.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


class TodoView(LoginRequiredMixin, View):
    login_url = reverse_lazy('dashboard:login')

    def get(self, request):
        d = {}
        todos = Todo.objects.filter(author=request.user)
        d['todos'] = todos

        return render(request, 'todo.html', context=d)


class EmailListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'email-inbox.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


class EmailReadView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'email-read.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


class ProfileView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')

    def get(self, request):
        code = request.user.code
        d = {}
        # print(client.service.GetProductBalance())
        d['business_reg'] = client.service.GetBusinessRegions(code)
        d['price_list'] = client.service.GetPriceTypes(code)
        d['sklad'] = client.service.GetWarehousesUser(code)
        d['gps'] = client.service.GetGPS(code, '20240921110122')[:6]
        recently_clients = Client.objects.filter(codeRegion=d['business_reg'][0]['Code']).order_by('-created_at')[:5]
        active_clients = Order.objects.filter(agent=request.user).select_related('client', ).values('clientCode',
                                                                                                    'clientName').annotate(
            Count("clientCode")).order_by('-clientCode__count')
        passive_clients = list(Order.objects.filter(agent=request.user).select_related('client', ).values('clientCode',
                                                                                                          'clientName').annotate(
            Count("clientCode")).order_by('clientCode__count'))
        d['recently_clients'] = recently_clients
        d['active_clients'] = active_clients[:5]
        d['passive_clients'] = passive_clients[:5]
        d['gallery_images'] = VisitingImages.objects.filter(author=request.user)[:5]
        print(d['passive_clients'])
        return render(request, 'profile.html', context=d)


class UserListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('dashboard:login')

    def get(self, request):
        d = {}
        clientlist = client.service.GetClients(request.user.code)
        d['clients'] = clientlist
        return render(request, 'user-list.html', context=d)


class ClientProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('dashboard:login')

    def get(self, request, pk):
        pass


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'product-list.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')

    def get(self, request):
        d = {}
        codeSklad = request.user.codeSklad.code
        codeProject = request.user.codeProject.code
        products = GetProductsBlance_sync(code_project=codeProject, code_sklad=codeSklad)
        d['products'] = products
        return render(request, 'product-list.html', context=d)

    def post(self, request):
        d = {}
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
        d['products'] = products[:21]
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
        Clients_sync(request.user.code)
        Orders_sync(request.user.code)
        OrderDetails_sync(request.user.code)
        return redirect('dashboard:index')
