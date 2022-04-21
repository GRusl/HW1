from django import forms


class UserUpdateForm(forms.Form):
    email = forms.EmailField(label='email')
    name = forms.CharField(label='Имя', required=False)
    birthday = forms.DateField(label='День рождения', required=False)
