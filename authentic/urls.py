from django.urls import path, include, reverse_lazy
from .views import LoginView, RegisterView, UserEditView, Connect1CView
from django.contrib.auth import views as auth_views

app_name = 'authentic'
urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("authentic:password_change_done")),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy("authentic:password_reset_done")),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy("authentic:password_reset_complete")),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('user-edit', UserEditView.as_view(), name='user-edit'),
    path('connect-1c/', Connect1CView.as_view(), name='connect-1c'),
    path('', include('django.contrib.auth.urls')),
]
