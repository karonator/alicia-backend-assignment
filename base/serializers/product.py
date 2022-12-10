from rest_framework import serializers

from base.models import Product, ProductProperty


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'sku', 'short')


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        exclude = ('product',)


class ProductFullSerializer(serializers.ModelSerializer):
    properties = ProductPropertySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('__all__')
