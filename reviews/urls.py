from django.urls import path
from . import views

urlpatterns = [
    path('', views.productReview, name="product_review"),
]
