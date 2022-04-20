from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.db.models import Prefetch

from django.http import HttpResponse

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView

from rating.models import Rating
from users.models import Profile

from users.forms import UserUpdateForm


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


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'

    def get_success_url(self):
        return reverse('login')


def user_list(request):
    users = get_user_model().objects.only('username').filter(is_active=True)

    context = {'users': users}
    return render(request, 'users/user_list.html', context=context)


def user_detail(request, int_id):
    user = get_object_or_404(
        get_user_model().objects.only('first_name',
                                      'last_name', 'email').prefetch_related(
            Prefetch('profile', queryset=Profile.objects.only('birthday'))
        ), id=int_id)
    best_ratings = Rating.objects.get_best(user)

    context = {'user_': user, 'best_ratings': best_ratings}
    return render(request, 'users/user_detail.html', context=context)


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = UserUpdateForm(
                initial={
                    'name': request.user.first_name,
                    'email': request.user.email,
                    'birthday': request.user.profile.birthday,
                }
            )
            best_ratings = Rating.objects.get_best(request.user)

            context = {'form': form, 'best_ratings': best_ratings}
            return render(request, 'users/profile.html', context=context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            form = UserUpdateForm(request.POST or None)
            if form.is_valid():
                user = request.user
                user.first_name = form.cleaned_data['name']
                user.email = form.cleaned_data['email']
                user.save(update_fields=['first_name', 'email'])

                profile = user.profile
                profile.birthday = form.cleaned_data['birthday']
                profile.save(update_fields=['birthday'])

            return redirect('profile_home')
        return redirect('login')
