from django.core.validators import EmailValidator
from rest_framework import serializers

from leads.models import Lead
from products.models import Product


class LeadSerializer(serializers.ModelSerializer):
    interested_products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone_number', 'interested_products']
