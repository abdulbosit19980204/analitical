from audioop import reverse
from rest_framework.routers import SimpleRouter

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView, EcommerceView, CalendarView, ChatView, TodoView, EmailListView, EmailReadView, \
    ProfileView, UserListView, ErrorPageView, InvoiceView, ProductView, RefreshView, OrderHistoryView, \
    OrderDetailView, ProductDetailView, GetStatistics, GPS_dataView, ProductViewSet
from rest_framework.routers import DefaultRouter
from dashboard.views import SearchFilterViewSet

router = DefaultRouter()
router.register('search', SearchFilterViewSet)

app_name = 'dashboard'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('refresh/', RefreshView.as_view(), name='refresh'),
    path('ecommerce', EcommerceView.as_view(), name='ecommerce'),
    path('calendar', CalendarView.as_view(), name='calendar'),
    path('chat', ChatView.as_view(), name='chat'),
    path('todo', TodoView.as_view(), name='todo'),
    path('email', EmailListView.as_view(), name='email'),
    path('email/read', EmailReadView.as_view(), name='email-read'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

    path('user-list', UserListView.as_view(), name='user-list'),

    path('order-history/', OrderHistoryView.as_view(), name='order-history'),
    path('order-detail/<str:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('product/', ProductView.as_view(), name='product'),
    path('product/<int:product_id>', ProductDetailView.as_view(), name='product-detail'),
    path('error', ErrorPageView.as_view(), name='error'),
    path('invoice', InvoiceView.as_view(), name='invoice'),

    path('api/statistics/', GetStatistics.as_view(), name='get_statistics'),
    path('api/gps/', GPS_dataView.as_view(), name='gps'),

]

router = SimpleRouter()
router.register('products', ProductViewSet, 'products')
urlpatterns += router.urls
