from rest_framework import serializers

from base.models import Order, OrderItem, CartItem
from base.serializers import ProductShortSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductShortSerializer()

    class Meta:
        model = OrderItem
        exclude = ('order',)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(read_only=True, many=True)

    def create(self, validated_data):
        user = self.context.get('request').user
        cart = CartItem.objects.filter(user=user)
        validated_data['user'] = user
        order = Order.objects.create(**validated_data)
        for cart_item in cart:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                amount=cart_item.amount
            )
        cart.delete()
        return order

    class Meta:
        model = Order
        exclude = ('user', 'created')
