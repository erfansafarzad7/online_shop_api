from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ('quantity', 'product', 'product_id')
        depth = 3
