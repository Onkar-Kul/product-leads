from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'price']

    # Validation for price, Price should be greater than 0
    @staticmethod
    def validate_price(value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value
