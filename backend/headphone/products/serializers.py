from rest_framework import serializers

from .models import Rating, discount_product

class discont_product_serializers(serializers.ModelSerializer):
    class Meta:
            model = discount_product
            fields = '__all__'

class  rating_serializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'