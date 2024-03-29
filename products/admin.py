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
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
