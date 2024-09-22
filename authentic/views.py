import json
from email.policy import default
from http.client import responses
from xxlimited_35 import error

from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.views import View
from .forms import SignUpForm, UserEditForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from api.models import Project, Warehouse, CustomUser


# Create your views here.

class LoginView(generic.ListView):
    model = User
    template_name = 'login.html'
    context_object_name = 'users'


class RegisterView(UserPassesTestMixin, View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for you!')
            return redirect('/auth/login')
        return render(request, 'registration/register.html', {'form': form})

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return False
        return True


class UserEditView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentic:login')

    # form_class = UserEditForm

    def get(self, request):
        form = UserEditForm(instance=request.user)
        user = request.user
        data = {'form': form}
        return render(request, 'user-edit.html', {'form': form})

    def post(self, request):
        form = UserEditForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Information was updated successfully!')
            return redirect('dashboard:profile', )
        return render(request, 'user-edit.html', {'form': form, 'errors': form.errors})


class Connect1CView(View):
    def post(self, request):
        from .integrations import client
        user_1c = client.service.GetUser(request.POST['login-1c'], request.POST['password-1c'])
        user = request.user

        codeuser = CustomUser.objects.filter(code=user_1c.Code).first()
        print(codeuser)
        if user_1c.Code != None:
            if codeuser is None:
                lf = user_1c.Name.split(' ')
                user.c1_connected = True
                user.code = user_1c.Code
                user.first_name = lf[0]
                user.last_name = lf[1]

                # user.code = user_1c.Code
                # codeSklad1 = Warehouse.objects.all(code=user_1c.CodeProject).first()
                # project1 = Project.objects.all(code=user_1c.CodeProject).first()
                # if codeSklad1 != None and project1 != None:
                #     user.codeSklad = codeSklad1
                # user.codeProject = project1

                user.save(update_fields=['c1_connected', 'code', 'first_name', 'last_name'])
                return redirect('authentic:user-edit')
            else:
                error = f'User was connected to {codeuser.username}'
        else:
            error = 'Login or Password doesn\'t match'

        return render(request, 'user-edit.html', {'error': error, 'form': UserEditForm()})
