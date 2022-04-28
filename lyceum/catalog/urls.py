from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.ItemList.as_view(), name="catalog"),
    path("<int:int_id>/", views.ItemDetail.as_view(), name="item_detail"),
]
