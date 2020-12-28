from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Mtg_Cards, Mtg_Sets


def all_products(request):
    """ A view to show all products including sort and search queries"""

    products = Mtg_Cards.objects.all()
    query = None
    mtg_expansions = None

    if request.GET:
        if 'mtgexpansion' in request.GET:
            mtg_expansions = request.GET['mtgexpansion'].split(',')
            products = products.filter(mtg_set__name__in=mtg_expansions)
            mtg_expansions = Mtg_Sets.objects.filter(name__in=mtg_expansions)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(oracle_text__icontains=query) | Q(mtg_set__friendly_name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_expansions': mtg_expansions,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Mtg_Cards, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
