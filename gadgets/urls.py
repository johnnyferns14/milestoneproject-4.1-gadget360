from django.urls import path
from . import views

urlpatterns = [
    path('gadgets/', views.viewGadgets, name="gadgets"),
]
