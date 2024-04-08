from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UserChangeForm
)
from django.utils.translation import gettext as _
from django import forms

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            _('first_name'),
            _('last_name'),
            _('username'),
            _('password1'),
            _('password2'),
        ]


class UserUpdateForm(UserChangeForm):
    password = None

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            _('first_name'),
            _('last_name'),
            _('username'),
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            _('username'), _('password1'),
        ]
