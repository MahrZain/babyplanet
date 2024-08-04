# Generated by Django 5.0.6 on 2024-08-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_products_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='availability',
            field=models.CharField(choices=[('----', '----'), ('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock')], default='----', max_length=20, null=True),
        ),
    ]
