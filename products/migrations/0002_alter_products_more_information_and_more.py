# Generated by Django 5.0.6 on 2024-07-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='More_information',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='compare_price',
            field=models.IntegerField(blank=True),
        ),
    ]