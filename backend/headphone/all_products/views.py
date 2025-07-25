from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import all_products
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductViewSet(viewsets.ModelViewSet):
    queryset = all_products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]