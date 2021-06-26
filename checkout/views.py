from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping cart is empty")
        return redirect(reverse, 'gadgets')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form
    }

    return render(request, template, context)
