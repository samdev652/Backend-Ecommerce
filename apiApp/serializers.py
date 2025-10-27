from rest_framework import serializers
from .models import Product, Category


class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "image", "price"]

class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "image", "price"]

class CategorySerializers(serializers.ModelSerializers):
    products = ProductListSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ["id", "name", "image", "products "]