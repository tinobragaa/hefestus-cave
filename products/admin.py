from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'category',
        'description',
        'stock',
        'image'
    )

    ordering = ('name',)


admin.site.register(Product)
admin.site.register(Category)
