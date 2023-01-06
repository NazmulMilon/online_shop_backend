from rest_framework.serializers import ModelSerializer
from .models import Category, Book, Product
from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers


class CategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookCreateSerializer(ModelSerializer):
    category = serializers.IntegerField(required=True)

    class Meta:
        model = Book
        exclude = ['created_at', 'update_at']


class BookSerializer(ModelSerializer):
    category = SerializerMethodField()

    def get_category(self, instance):
        category_queryset = Category.objects.filter(id=instance.id)
        return CategoryRetrieveSerializer(category_queryset, many=True).data

    class Meta:
        model = Book
        exclude = ['update_at']
        # fields = [
        #     'id',
        #     'book_title',
        #     'category',
        #     'isbn',
        #     'pages',
        #     'book_price',
        #     'stock',
        #     'description',
        #     'image_url',
        #     'status',
        #     'created_at',
        # ]


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()

    def get_category(self, instance):
        category_queryset = Category.objects.filter(id=instance.id)
        return CategoryRetrieveSerializer(category_queryset, many=True).data

    class Meta:
        model = Product
        exclude = ['updated_at']
        # fields = (
        #     'id',
        #     'product_tag',
        #     'product_name',
        #     'category',
        #     'product_price',
        #     'stock',
        #     'image_url',
        #     'description',
        #     'status',
        #     'created_at'
        # )


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['updated_at']


class CategorySerializer(ModelSerializer):
    products = SerializerMethodField()

    def get_products(self, instance):
        product_queryset = Product.objects.filter(category_id=instance.id)
        return ProductListSerializer(product_queryset, many=True).data

    class Meta:
        model = Category
        fields = "__all__"
        # fields = [
        #     'id',
        #     'category_title'
        # ]
