# Generated by Django 5.0.6 on 2024-08-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_products_compare_price_remove_products_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price_that_you_sell',
            field=models.IntegerField(help_text='the price that you sell', null=True),
        ),
    ]
