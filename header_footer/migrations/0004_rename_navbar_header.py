# Generated by Django 5.0.6 on 2024-08-23 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0003_alter_footer_name_alter_navbar_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Navbar',
            new_name='Header',
        ),
    ]
