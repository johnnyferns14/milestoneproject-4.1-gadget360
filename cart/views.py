from django.shortcuts import render, redirect
from django.contrib import messages
from gadgets.models import gadgetAttr


def viewCart(request):
    return render(request, "cart/view_cart.html")


def addToCart(request, item_id):
    gadget = gadgetAttr.objects.get(asins=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Your item {gadget.name} has been added to the cart.')
    request.session["cart"] = cart
    print(request.session["cart"])
    return redirect(redirect_url)
