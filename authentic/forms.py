from django import forms
from api.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'username', 'phone_number')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'tg_username', 'tg_code', 'picture']
