# Generated by Django 5.0.6 on 2024-09-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userdata_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
