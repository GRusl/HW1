from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list),
    path('<int:int_id>/', views.ItemDetail.as_view(), name='item_detail'),
]
