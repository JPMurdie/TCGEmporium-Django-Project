from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Mtg_Cards, Mtg_Sets, Sales_Category
from .forms import ProductForm


def all_products(request):
    """ A view to show all products including sort and search queries"""

    products = Mtg_Cards.objects.all()
    query = None
    mtg_expansions = None
    stock_types = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'stocktype' in request.GET:
            stock_types = request.GET['stocktype'].split(',')
            products = products.filter(sales_category__name__in=stock_types)
            stock_types = Sales_Category.objects.filter(name__in=stock_types)

        if 'mtgexpansion' in request.GET:
            mtg_expansions = request.GET['mtgexpansion'].split(',')
            products = products.filter(mtg_set__name__in=mtg_expansions)
            mtg_expansions = Mtg_Sets.objects.filter(name__in=mtg_expansions)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(oracle_text__icontains=query) | Q(mtg_set__friendly_name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_expansions': mtg_expansions,
        'current_stocktype': stock_types,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Mtg_Cards, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
