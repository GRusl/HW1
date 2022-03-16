from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:int_id>/', views.user_detail),
    path('signup/', views.signup),
    path('profile/', views.profile)
]
