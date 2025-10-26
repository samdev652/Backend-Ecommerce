from rest_framework import serializers
from .models import Product, Category


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "image", "price"]


class CategorySerializers(serializers.ModelSerializers):
    products = ProductSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ["id", "name", "image", "products "]