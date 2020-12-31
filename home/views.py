from django.shortcuts import render
from products.models import Mtg_Cards


def index(request):
    """ A view to return the index page """

    products = Mtg_Cards.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
