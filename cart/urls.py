from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewCart, name="view_cart"),
    path('add/<item_id>/', views.addToCart, name="add_to_cart"),
]
