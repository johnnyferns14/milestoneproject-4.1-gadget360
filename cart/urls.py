from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.addToCart, name="add_to_cart"),
]
