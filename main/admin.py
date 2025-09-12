# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_featured', 'product_views')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'description')
