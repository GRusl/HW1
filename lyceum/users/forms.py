from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserUpdateForm(forms.Form):
    email = forms.EmailField(label="email")
    name = forms.CharField(label="Имя", required=False)
    birthday = forms.DateField(label="День рождения", required=False)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("email", )
