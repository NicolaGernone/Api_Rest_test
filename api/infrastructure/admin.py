from django.contrib import admin

from .models import *


@admin.register(Data)
class ImageAdmin(admin.ModelAdmin):
    list_display=('sno', 'name', 'symbol', 'date', 'hight', 'low', 'open', 'close', 'volume', 'marketcap')
