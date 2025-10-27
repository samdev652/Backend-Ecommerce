from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
from .serializers import ProductListSerializer, ProductDetailSerializer

# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all() 
    serializer = ProductListSerializer(products, many=True)  
    return  Response(serializer.data)

@api_view(['GET'])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])