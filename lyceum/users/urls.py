from django.urls import path
from django.contrib.auth.views import (LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView,
                                       PasswordChangeView, PasswordChangeDoneView)

from users import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:int_id>/', views.user_detail),

    path('signup/', views.SignupView.as_view()),
    path('profile/', views.ProfileView.as_view(), name='profile_home'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('password_change/',
         PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),

    path('password_reset/',
         PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
