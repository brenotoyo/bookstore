from rest_framework import serializers

from product.models import Product, Category
from product.serializers.category_serialiazer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'active',
            'categories',
        ]

    def create(self, validated_data):
        categories_data = validated_data.pop("categories", [])
        product = Product.objects.create(**validated_data)
        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(**category_data)
            product.categories.add(category)
        return product