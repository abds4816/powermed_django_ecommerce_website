from django.contrib import admin
from .models import Category, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'category',)
    list_display = ('name', 'price', 'old_price', 'is_active',)
    list_editable = ('price', 'old_price', 'is_active',)
    search_fields = ('name',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)