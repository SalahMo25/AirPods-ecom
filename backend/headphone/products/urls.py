from django.urls import path
from . import api
urlpatterns = [
    path('discount_product' , api.discount_products.as_view(), name='discount_products'),
    path('discount_product_detail/<int:pk>' , api.discont_product_details, name='discount_product_detail'),
    path('rating' , api.create_rating, name='rating'),
]