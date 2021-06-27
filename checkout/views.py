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
        'order_form' : order_form,
        'stripe_public_key': 'pk_test_51J6mAXBFIa4qhUqSs9AXeoU959DOv163Wge7al6D9juKQOshnqYcoWwXIeRRNtKJzVjs7kPGg6cykf0ZzPvIbYce00BEZq1aEq',
        'client_secret' : 'sk_test_51J6mAXBFIa4qhUqSW0nvQi446eYFMRz9gBBoHeLJf73SROZZdAFyXJrjY0Jv37ACgrhGiv2LdLidPa0Edlzsg2aC00z4NkxV8m'
    }

    return render(request, template, context)
