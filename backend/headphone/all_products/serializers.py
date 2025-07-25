from rest_framework import serializers
from .models import all_products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_products
        fields = '__all__'