import io
import base64
from django.contrib import admin
from .models import Items


class itemsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    list_filter = ("name", "price")

admin.site.register(Items, itemsAdmin)
