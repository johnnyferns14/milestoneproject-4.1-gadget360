from django.urls import path
from . import views

urlpatterns = [
    path('<gadget_id>', views.checkout, name="checkout"),
]
