from http import HTTPStatus

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

from django.http import HttpResponse

from django.shortcuts import render, reverse


def user_list(request):
    return render(request, 'users/user_list.html')


def user_detail(request, int_id):
    if int_id in (1, ):
        return render(request, 'users/user_detail.html')

    return HttpResponse(status=HTTPStatus.NOT_FOUND)


def signup(request):
    return render(request, 'users/signup.html')


def profile(request):
    return render(request, 'users/profile.html')


class LoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('profile_home')


class LogoutView(LogoutView):
    next_page = '/'


class PasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class PasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
