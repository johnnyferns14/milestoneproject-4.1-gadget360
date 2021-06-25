from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewGadgets, name="gadgets_view"),
    path('<gadget_id>', views.checkout, name="checkout"),
]
