from django.core.validators import EmailValidator
from rest_framework import serializers

from leads.models import Lead
from products.models import Product
from products.serializers import ProductSerializer


class LeadSerializer(serializers.ModelSerializer):
    interested_products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone_number', 'interested_products']

    def validate(self, data):
        if not data.get('email'):
            raise serializers.ValidationError("Email is required.")
        if not data.get('phone_number'):
            raise serializers.ValidationError("Phone number is required.")

        if not data.get('email') and not data.get('phone_number'):
            raise serializers.ValidationError("Either email or phone number must be provided.")

        return data

    @staticmethod
    def validate_phone_number(value):
        if not value.startswith('+') or not value[1:].isdigit() or len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError(
                "Phone number must be in the format: +999999999999.")
        return value


class LeadProductCount(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    interested_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone_number', 'product_count', 'interested_products', 'created_at']
        read_only_fields = fields
