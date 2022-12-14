from django.contrib import admin

from base.models import Product, ProductProperty, CartItem, Order, OrderItem


class ProductPropertyAdmin(admin.TabularInline):
    model = ProductProperty


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "sku", "price")
    inlines = [
        ProductPropertyAdmin,
    ]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "amount")


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "delivery_time")
    inlines = [
        OrderItemAdmin,
    ]
