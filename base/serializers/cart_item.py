from rest_framework import serializers

from base.models import CartItem
from base.serializers import ProductShortSerializer


class CartItemSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        amount = validated_data.pop('amount')
        item, _ = CartItem.objects.get_or_create(**validated_data)
        item.amount += amount
        item.save()
        return item

    class Meta:
        model = CartItem
        exclude = ('user',)


class CartItemFullSerializer(serializers.ModelSerializer):
    product = ProductShortSerializer(read_only=True)

    class Meta:
        model = CartItem
        exclude = ('user',)
