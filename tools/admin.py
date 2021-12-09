from typing import List
from django.contrib import admin
from . models import Tools

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description')

admin.site.register(Tools, ProductAdmin)