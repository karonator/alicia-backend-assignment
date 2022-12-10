from django.contrib import admin

from base.models import Product, ProductProperty, CartItem


class ProductPropertyAdmin(admin.TabularInline):
    model = ProductProperty


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'price')
    inlines = [ProductPropertyAdmin, ]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'amount')
