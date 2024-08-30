# Generated by Django 5.0.6 on 2024-08-28 06:31

import offer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_alter_offer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.FileField(help_text='Image size must be 1920x800 pixels', max_length=60, upload_to='products/', validators=[offer.models.validate_image_size]),
        ),
    ]
