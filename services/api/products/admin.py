from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code', 'position', 'quantity',
        'image', 'price', 'description'
    )


admin.site.register(Product, ProductAdmin)
