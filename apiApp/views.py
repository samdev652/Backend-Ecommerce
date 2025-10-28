from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product, Category
from rest_framework.response import Response
from .serializers import ProductListSerializers, ProductDetailSerializers, CategoryListSerializers, CategoryDetailSerializers


# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all() 
    serializer = ProductListSerializers(products, many=True)  
    return  Response(serializer.data)

@api_view(['GET'])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductDetailSerializers(product)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
   category = Category.objects.all()
   serializer = CategoryListSerializers(categories, many=True) 
   return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializers(category)
    return Response(serializer.data)
