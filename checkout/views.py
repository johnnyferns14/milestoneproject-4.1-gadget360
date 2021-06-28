from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from gadgets.models import gadgetAttr
from .models import OrderDetail, OrderLineItem
from cart.contexts import cartItems

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'cust_name': request.POST['cust_name'],
            'email_id': request.POST['email_id'],
            'contact_number': request.POST['contact_number'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'county': request.POST['county']
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order_form.save()
            for item_id, quantity in cart.items():
                try:
                    product = gadgetAttr.objects.get(asins=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity
                    )
                    order_line_item.save()

                except gadgetAttr.DoesNotExist:
                    messages.error(request, 'Item not found in database')
                    order.delete()
                    return redirect(reverse('viewCart'))
            
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your shopping cart is empty")
            return redirect(reverse, 'gadgets')

        cart_present = cartItems(request)
        total = cart_present['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(OrderDetail, order_number=order_number)
    messages.success(request, f'Order {order_number} created succesfully. \
                     A confirmation email will be sent to {order.email}')
    
    if 'cart' in request.session:
        del request.session['cart']
    
    template = 'checkout/checkout_success.html'

    context = {
        'order': order
    }

    return render(request, template, context)
