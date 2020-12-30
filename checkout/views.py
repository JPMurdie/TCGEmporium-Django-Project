from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag of holding has a hole in it!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H9agYCo72PB3Z3pe5v35VjcjnYRJNIAWUK9AiGVCABYj0HkWO13F5Wg4XxvQVAs8GuMQ9LzjbOcAV2ULOQdgkqN00lOfFstmS',
        'client_secret': 'test-secret-key'
    }

    return render(request, template, context)
