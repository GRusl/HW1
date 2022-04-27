from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from django.db.models import Prefetch

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView

from rating.models import Rating
from users.models import Profile

from users.forms import UserUpdateForm, RegisterForm


class LoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("auth:profile_home")


class SignupView(CreateView):
    form_class = RegisterForm
    template_name = "users/signup.html"

    def get_success_url(self):
        return reverse("auth:login")


class UserList(View):
    def get(self, request):
        users = get_user_model().objects.only("email").filter(is_active=True)

        context = {"users": users}
        return render(request, "users/user_list.html", context=context)


class UserDetail(View):
    def get(self, request, int_id):
        user = get_object_or_404(
            get_user_model()
                .objects.only("first_name", "last_name", "email")
                .prefetch_related(
                Prefetch("profile", queryset=Profile.objects.only("birthday"))
            ),
            id=int_id,
        )
        best_ratings = Rating.objects.get_best(user)

        context = {"user_": user, "best_ratings": best_ratings}
        return render(request, "users/user_detail.html", context=context)


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = UserUpdateForm(
                initial={
                    "name": request.user.first_name,
                    "email": request.user.email,
                    "birthday": request.user.profile.birthday,
                }
            )
            best_ratings = Rating.objects.get_best(request.user)

            context = {"form": form, "best_ratings": best_ratings}
            return render(request, "users/profile.html", context=context)
        return redirect("auth:login")

    def post(self, request):
        if request.user.is_authenticated:
            form = UserUpdateForm(request.POST or None)
            if form.is_valid():
                user = request.user
                user.first_name = form.cleaned_data["name"]
                user.email = form.cleaned_data["email"]
                user.save(update_fields=["first_name", "email"])

                profile = user.profile
                profile.birthday = form.cleaned_data["birthday"]
                profile.save(update_fields=["birthday"])

            return redirect("auth:profile_home")
        return redirect("auth:login")
