from django.db import models


class Sales_Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Mtg_Sets(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Mtg_Cards(models.Model):
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    lang = models.CharField(max_length=32, blank=True)
    type_line = models.CharField(max_length=254, blank=True)
    oracle_text = models.CharField(max_length=254, blank=True)
    power = models.CharField(max_length=8, blank=True)
    toughness = models.CharField(max_length=8, blank=True)
    colors = models.JSONField(default=list)
    color_identity = models.JSONField(default=list)
    mtg_set = models.ForeignKey('Mtg_Sets', null=True, blank=True, on_delete=models.SET_NULL)
    rarity = models.CharField(max_length=8, blank=True)
    collector_number = models.CharField(max_length=8, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sales_category = models.ForeignKey('Sales_Category', null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.CharField(max_length=32, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
