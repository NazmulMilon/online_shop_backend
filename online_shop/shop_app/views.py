from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, \
    CreateAPIView
from .models import Category, Book, Product
from .serializers import CategorySerializer, BookSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError


#
# # Create your views here.
#
class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        category_title = data.get('category_title', None)
        category_obj = Category(category_title=category_title)
        category_obj.save()
        return Response(data={'details': 'Category Added'}, status=status.HTTP_201_CREATED)


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        category_qs = self.queryset.filter(pk=kwargs['pk']).first()
        # print(category_qs)
        # category_obj = category_qs.first()
        if category_qs is None:
            return Response(data={'details': 'There is no data regarding this id'}, status=status.HTTP_404_NOT_FOUND)
            # raise ValidationError
        serializer = CategorySerializer(category_qs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        book_title = data.get('book_title', None)
        category = data.get('category', None)
        isbn = data.get('isbn', None)
        author_name = data.get('author_name', None)
        pages = data.get('pages', None)
        book_price = data.get('book_price', None)
        stock = data.get('stock', None)
        description = data.get('description', None)
        image_url = data.get('image_url', None)
        book_obj = Book(book_title=book_title, category_id=category, isbn=isbn, author_name=author_name, pages=pages,
                        book_price=book_price, stock=stock, description=description, image_url=image_url)
        book_obj.save()
        return Response(data={'details': 'New Book added.'}, status=status.HTTP_201_CREATED)


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        book_queryset = Book.objects.filter(pk=kwargs['pk']).first()
        if book_queryset is None:
            return Response(data={'details': 'Data is not available for this id. '}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book_queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class CategoryListAPIView(ListCreateAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#
#
# class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#
#
# class BookListAPIView(ListCreateAPIView):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()
#
#
# class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()
#
#
# class ProductListAPIView(ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#
# class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
