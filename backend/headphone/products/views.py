# from django.shortcuts import render
# from rest_framework import generics

# from .serializers import discont_product_serializers

# from .models import discount_product
# # Create your views here.

# class discount_products(generics.ListCreateAPIView):
#     queryset = discount_product.objects.all()
#     serializer_class = discont_product_serializers

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         # ...

#         return token
    
# class MyTokenObtainPairview(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer