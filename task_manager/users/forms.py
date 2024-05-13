from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UserChangeForm
)
from django import forms

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]


class UserUpdateForm(UserChangeForm):
    password = None

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username', 'password1',
        ]
