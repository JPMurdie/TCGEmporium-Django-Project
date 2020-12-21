from django.contrib import admin
from .models import Mtg_Cards, Mtg_Sets, Sales_Category


admin.site.register(Mtg_Cards)
admin.site.register(Mtg_Sets)
admin.site.register(Sales_Category)
