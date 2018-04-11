from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(BLProduct)
admin.site.register(BLImage)
admin.site.register(BLPriceHistory)
