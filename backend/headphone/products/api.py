from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import discont_product_serializers, rating_serializers

from .models import discount_product



# Create your views here.




class discount_products(generics.ListCreateAPIView):
    queryset = discount_product.objects.all()
    serializer_class = discont_product_serializers
    permission_classes = [AllowAny]

@api_view(['GET'])
@permission_classes([AllowAny])

def discont_product_details(request , pk):
    try:
        product = discount_product.objects.get(pk=pk)
    except discount_product.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = discont_product_serializers(product).data
    return Response(data)



@api_view(['POST'])
@permission_classes([AllowAny])

def create_rating(request):
    data = rating_serializers(data = request.data)
    
    if data.is_valid():
        product = data.validated_data['product']
        value = data.validated_data['value']
        
        product.all_ratings += 1
        product.rating = ((product.rating * product.all_ratings -1) + value) / product.all_ratings
        
        product.save()
        
        data.save()
        
        return Response(data.data, status=status.HTTP_201_CREATED)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)




        