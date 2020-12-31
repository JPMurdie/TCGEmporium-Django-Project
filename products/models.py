from django.db import models


class Sales_Category(models.Model):

    class Meta:
        verbose_name_plural = "Sales_Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Mtg_Sets(models.Model):

    class Meta:
        verbose_name_plural = "Mtg_Sets"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


def jsonfield_default_value():  # This is a callable
    return [0, 0]


Condition_Choices = (
    ('mint', 'Mint'),
    ('near_mint', 'Near Mint'),
    ('excellent', 'Excellent'),
    ('good', 'Good'),
    ('light_played', 'Light Played'),
    ('played', 'Played'),
    ('poor', 'Poor')
)

Foil_Choices = (
    ('non_foil', 'Non-Foil'),
    ('foil', 'Foil')
)

Collector_Choices = (
    ('normal', 'Normal'),
    ('showcase', 'Showcase'),
    ('expedition', 'Expedition'),
    ('textless', 'Textless')
)

Rarity_Choices = (
    ('Common', 'common'),
    ('Uncommon', 'uncommon'),
    ('Rare', 'rare'),
    ('Mythic', 'mythic'),
)


class Mtg_Cards(models.Model):

    class Meta:
        verbose_name_plural = "Mtg_Cards"

    sku = models.CharField(max_length=254, blank=False)
    name = models.CharField(max_length=254, blank=False)
    lang = models.CharField(max_length=32, blank=True)
    type_line = models.CharField(max_length=254, blank=True)
    oracle_text = models.CharField(max_length=1024, blank=True)
    mtg_set = models.ForeignKey('Mtg_Sets', null=True, blank=True, on_delete=models.SET_NULL)
    rarity = models.CharField(max_length=32, choices=Rarity_Choices, default='common')
    card_condition = models.CharField(max_length=12, choices=Condition_Choices, default='mint')
    card_print = models.CharField(max_length=12, choices=Foil_Choices, default='non_foil')
    card_collection_type = models.CharField(max_length=12, choices=Collector_Choices, default='normal')
    collector_number = models.IntegerField(choices=[(x, x) for x in range(1, 500)], default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    sales_category = models.ForeignKey('Sales_Category', null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.CharField(max_length=32, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
