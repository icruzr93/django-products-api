from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'code', 'position', 'quantity',
            'image', 'price', 'description'
        )
