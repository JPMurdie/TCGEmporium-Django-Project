# Generated by Django 3.1.4 on 2020-12-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201227_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtg_cards',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
