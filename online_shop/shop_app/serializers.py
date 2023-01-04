from rest_framework.serializers import ModelSerializer
from .models import Category, Book, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'category_title'
        ]


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'book_title',
            'category',
            'isbn',
            'pages',
            'book_price',
            'stock',
            'description',
            'image_url',
            'status',
            'created_at',
        ]


class ProductSerializer(ModelSerializer):
    class Meta:

        model = Product
        fields = (
            'id',
            'product_tag',
            'product_name',
            'category',
            'product_price',
            'stock',
            'image_url',
            'description',
            'status',
            'created_at'
        )

