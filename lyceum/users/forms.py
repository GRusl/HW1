from django import forms


class UserUpdateForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    birthday = forms.DateField()
