from django.contrib.auth.models import User
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout

from api.models import Warehouse, Organization
from authentic.integrations import client, GetDailyReport, werehouse


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


# class IndexView(LoginRequiredMixin, generic.ListView):
#     model = User
#     template_name = 'index.html'
#     context_object_name = 'users'
#     login_url = reverse_lazy('authentic:login')


class EcommerceView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'ecommerce.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'calendar.html'
    login_url = reverse_lazy('dashboard:login')


class ChatView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'chat.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


class TodoView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'todo.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


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


# class UserListView(LoginRequiredMixin, generic.ListView):
#     model = User
#     template_name = 'user-list.html'
#     context_object_name = 'users'
#     login_url = reverse_lazy('dashboard:login')


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'product-list.html'
    context_object_name = 'users'
    login_url = reverse_lazy('dashboard:login')


class ProductView(generic.ListView):
    model = User
    template_name = 'product.html'
    context_object_name = 'users'


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
        c_warehouses = client.service.GetWarehouses()
        c_organizations = client.service.GetOrganizations()
        warehouse_list = []
        organizations_list = []
        for i in c_organizations:
            if not Organization.objects.filter(code=i['Code']).exists():
                organization = Organization(code=i['Code'], name=i['Name'])
                organizations_list.append(organization)
        Organization.objects.bulk_create(organizations_list)
        for i in c_warehouses:
            # Get the Organization object based on i['Organization']
            organization = Organization.objects.filter(code=i['Organization']).first()
            # Check if the warehouse already exists based on unique fields (e.g., name and organization)
            if not Warehouse.objects.filter(name=i['Name'], organization=organization).exists():
                # Create the Warehouse object
                warehouse = Warehouse(
                    name=i['Name'],
                    code=i['Code'],  # Replace with correct field from i
                    organization=organization  # Assign the foreign key here
                )
                warehouse_list.append(warehouse)

        # Bulk create new warehouses
        Warehouse.objects.bulk_create(warehouse_list)

        return redirect('dashboard:index')
