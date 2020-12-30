from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag of holding has a hole in it!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H9agYCo72PB3Z3pe5v35VjcjnYRJNIAWUK9AiGVCABYj0HkWO13F5Wg4XxvQVAs8GuMQ9LzjbOcAV2ULOQdgkqN00lOfFstmS',
        'client_secret': 'test-secret-key'
    }

    return render(request, template, context)
