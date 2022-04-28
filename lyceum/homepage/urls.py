from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.Home.as_view(), name="homepage")
]
