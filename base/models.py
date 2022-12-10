from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Title'
    )
    sku = models.CharField(
        max_length=64,
        verbose_name='SKU'
    )
    short = models.CharField(
        max_length=256, null=True, blank=True,
        verbose_name='Short description'
    )
    full = models.TextField(
        null=True, blank=True,
        verbose_name='Short description'
    )
    price = models.FloatField(
        default=0,
        verbose_name='Price'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# just for example, ofc...
class ProductProperty(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, related_name='properties',
        verbose_name='Product'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Title'
    )
    value = models.CharField(
        max_length=256,
        verbose_name='Value'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Product property'
        verbose_name_plural = 'Products properties'


class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='User'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    amount = models.IntegerField(
        default=0,
        verbose_name='Amount'
    )

    class Meta:
        ordering = ('user',)
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='User'
    )
    delivery_time = models.DateTimeField(
        verbose_name='Date'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created'
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Order',
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    amount = models.IntegerField(
        default=0,
        verbose_name='Amount'
    )

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'
