from django.shortcuts import render
from .models import Mtg_Cards


def all_products(request):
    """ A view to show all products including sort and search queries"""

    products = Mtg_Cards.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
