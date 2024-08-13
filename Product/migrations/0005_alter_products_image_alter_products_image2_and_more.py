# Generated by Django 5.0.6 on 2024-08-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_products_image4_products_image5_products_image6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.FileField(help_text='Image size must be 500 X 500 pixels and add all images. If you dont have enough images then you can add 1 image 6 times', null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.FileField(help_text='Image size must be 500 X 500 pixels and add all images. If you dont have enough images then you can add 1 image 6 times', null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=models.FileField(help_text='Image size must be 500 X 500 pixels and add all images. If you dont have enough images then you can add 1 image 6 times', null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image4',
            field=models.FileField(help_text='Image size must be 500 X 500 pixels and add all images. If you dont have enough images then you can add 1 image 6 times', null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image5',
            field=models.FileField(help_text='Image size must be 500 X 500 pixels and add all images. If you dont have enough images then you can add 1 image 6 times', null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image6',
            field=models.FileField(help_text='Image size must be 500 X 500 pixels and add all images. If you dont have enough images then you can add 1 image 6 times', null=True, upload_to='products/'),
        ),
    ]