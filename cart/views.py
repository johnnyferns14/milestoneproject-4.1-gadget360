from django.shortcuts import render

def addToCart(request):
    return render(request, "cart/add_to_cart.html")
