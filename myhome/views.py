from django.shortcuts import render
from .models import productInfo


products = productInfo.objects.all()

def home(request):
    context = {
        "products" : products
    }

    return render(request, "myhome/index.html", context)
