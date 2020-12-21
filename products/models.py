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
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    lang = models.CharField(max_length=25)
    type_line = models.CharField(max_length=254)
    oracle_text = models.CharField(max_length=254)
    power = models.CharField(max_length=5)
    toughness = models.CharField(max_length=5)
    colors = ListCharField(encoder=None, decoder=None)
    color_identity =
    mtg_set = models.ForeignKey('Mtg_Sets', null=False, blank=False)
    rarity =
    collector_number =
    price =
    sales_category = models.ForeignKey('Sales_Category', null=False, blank=False)
    artist =
    image_url =
    image =