from django.shortcuts import render, redirect


def viewCart(request):
    return render(request, "cart/view_cart.html")


def addToCart(request, item_id):
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] +=quantity
    else:
        cart[item_id] = quantity
    
    request.session["cart"] = cart
    print(cart)
    return redirect(redirect_url)
