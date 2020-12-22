from django.contrib import admin
from .models import Mtg_Cards, Mtg_Sets, Sales_Category


class MtgCardsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'mtg_set',
        'sales_category',
        'price',
        'image',
    )

    ordering = ('pk',)


class SalesCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )


class MtgSetsAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )


admin.site.register(Mtg_Cards, MtgCardsAdmin)
admin.site.register(Mtg_Sets, MtgSetsAdmin)
admin.site.register(Sales_Category, SalesCategoryAdmin)
