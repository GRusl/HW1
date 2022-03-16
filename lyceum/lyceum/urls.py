from django.contrib import admin
from django.urls import path

from homepage import views as homepage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_views.home)
]
