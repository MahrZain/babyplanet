# Generated by Django 5.0.6 on 2024-08-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header_footer', '0005_rename_name_footer_title_remove_footer_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footersection',
            name='footer',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='title',
        ),
        migrations.AddField(
            model_name='footer',
            name='create',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='header',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='FooterLink',
        ),
        migrations.DeleteModel(
            name='FooterSection',
        ),
    ]