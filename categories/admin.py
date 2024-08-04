from django.contrib import admin
from .models import Category
class categoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'image']
admin.site.register(Category , categoryAdmin)