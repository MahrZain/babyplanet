# Generated by Django 5.0.6 on 2024-08-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.CharField(default='unpaid', max_length=20, null=True),
        ),
    ]