from django.urls import path, include
from .views import LoginView, RegisterView, UserEditView, Connect1CView
from django.contrib.auth import views as auth_views

app_name = 'authentic'
urlpatterns = [
    # path('login', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_changed/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('user-edit', UserEditView.as_view(), name='user-edit'),
    path('connect-1c/', Connect1CView.as_view(), name='connect-1c'),
    path('', include('django.contrib.auth.urls')),
]
