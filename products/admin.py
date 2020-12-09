from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'rating',
        'image',

    )

    oredring = ('id')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
