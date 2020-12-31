from django import forms
from .models import Mtg_Cards, Mtg_Sets, Sales_Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Mtg_Cards
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        categories = Sales_Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        mtg_sets = Mtg_Sets.objects.all()
        mtg_sets_friendly_names = [(c.id, c.get_friendly_name()) for c in mtg_sets]

        self.fields['sales_category'].choices = friendly_names
        self.fields['mtg_set'].choices = mtg_sets_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
