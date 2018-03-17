from django.contrib import admin

# Register your models here.
from .models import Brand, Item

admin.site.register(Brand)
admin.site.register(Item)