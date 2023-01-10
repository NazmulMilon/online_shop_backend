import json

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView
from .models import Category, Book, Product
from .serializers import CategorySerializer, BookSerializer, ProductSerializer, CategoryRetrieveSerializer, \
    BookCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from django.http.response import HttpResponse, JsonResponse


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
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        category_qs = self.queryset.filter(pk=kwargs['pk']).first()
        # print(category_qs)
        # category_obj = category_qs.first()
        if category_qs is None:
            return Response(data={'details': 'There is no data regarding this id'}, status=status.HTTP_404_NOT_FOUND)
            # raise ValidationError
        serializer = CategoryRetrieveSerializer(category_qs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        category_qs = Category.objects.filter(id=pk).update(**request.data)
        return Response(data={'details': 'Category data updated. '}, status=status.HTTP_200_OK)


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookCreateSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        category_obj = None
        data = request.data
        book_title = data.get('book_title', None)
        if book_title is None:
            return Response(data={'Details': 'Book title required. '}, status=status.HTTP_400_BAD_REQUEST)
        category = data.get('category', None)
        if category is None:
            return Response(data={'details': 'Category name required. '}, status=status.HTTP_400_BAD_REQUEST)

        # if not Category.objects.filter(id=category["id"]).exists():
        #     # return Response(data={'Details': "Category Doesn't Exist"}, status=status.HTTP_400_BAD_REQUEST)
        #     if not Category.objects.filter(category_title=category["name"]).exists():
        #         # return Response(data={'Details': "Category name Doesn't Exist"}, status=status.HTTP_400_BAD_REQUEST)
        #         # Category.objects.create(category_title=name)
        #         category_obj = Category(id=id, category_title=name)
        #         category_obj.save()
        # id = category["id"]
        # name = category["name"]

        # if "id" in request.data["category"]:
        if "id" in request.data["category"].keys():
            # return Response(data={'details': "category id doesn't exist. "})
            category_obj = Category.objects.filter(id=category["id"]).first()
            if not category_obj:
                return Response(data={'details': "category id doesn't exist. "})
        # elif "name" in request.data["category"].keys():
        elif "name" in request.data["category"]:
            category_obj = Category.objects.filter(category_title=category["name"]).first()
            if not category_obj:
                category_obj = Category.objects.create(category_title=category["name"])

        # if Category.objects.filter(category_title=category["name"]).exists():
        #     return Response(data={'details': 'category name exists. '}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     Category.objects.create(category_title=category["name"])
        isbn = data.get('isbn', None)
        author_name = data.get('author_name', None)
        pages = data.get('pages', None)
        book_price = data.get('book_price', None)
        if book_price < 50:
            return Response(data={'Details': 'Price must be above 50. '}, status=status.HTTP_400_BAD_REQUEST)
        stock = data.get('stock', None)
        if stock < 5:
            return Response(data={'Details': 'Stock must be at least 5. '}, status=status.HTTP_400_BAD_REQUEST)
        description = data.get('description', None)
        if len(description) <= 20 or len(description) >= 1000:
            return Response(data={'Details': 'Length must be between 20 to 1000. '}, status=status.HTTP_400_BAD_REQUEST)

        image_url = data.get('image_url', None)
        book_obj = Book(book_title=book_title, category_id=category_obj.id, isbn=isbn, author_name=author_name,
                        pages=pages, book_price=book_price, stock=stock, description=description, image_url=image_url)
        book_obj.save()
        serializer = BookSerializer(book_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


#
# class BookCreateAPIView(CreateAPIView):
#     serializer_class = BookCreateSerializer
#     queryset = Book.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         book_title = data.get('book_title', None)
#         if book_title is None:
#             return Response(data={'Details': 'Book title required. '}, status=status.HTTP_400_BAD_REQUEST)
#         category = data.get('category', None)
#         # if category is None:
#         #     return Response(data={'details': 'Category name required. '}, status=status.HTTP_400_BAD_REQUEST)
#         if not Category.objects.filter(id=category).exists():
#             return Response(data={'Details': "Category Doesn't Exist"}, status=status.HTTP_400_BAD_REQUEST)
#         isbn = data.get('isbn', None)
#         author_name = data.get('author_name', None)
#         pages = data.get('pages', None)
#         book_price = data.get('book_price', None)
#         if book_price < 50:
#             return Response(data={'Details': 'Price must be above 50. '}, status=status.HTTP_400_BAD_REQUEST)
#         stock = data.get('stock', None)
#         if stock < 5:
#             return Response(data={'Details': 'Stock must be at least 5. '}, status=status.HTTP_400_BAD_REQUEST)
#         description = data.get('description', None)
#         if len(description) <= 20 or len(description) >= 1000:
#             return Response(data={'Details': 'Length must be between 20 to 1000. '},
#             status=status.HTTP_400_BAD_REQUEST)
#
#         image_url = data.get('image_url', None)
#         book_obj = Book(book_title=book_title, category_id=category, isbn=isbn, author_name=author_name, pages=pages,
#                         book_price=book_price, stock=stock, description=description, image_url=image_url)
#         book_obj.save()
#         return Response(data={'details': 'New Book added.'}, status=status.HTTP_201_CREATED)
#

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
        book_obj = Book.objects.filter(pk=kwargs['pk']).first()
        if book_obj is None:
            return Response(data={'details': 'Data is not available for this id. '}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookUpdateAPIView(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        book_queryset = Book.objects.filter(id=pk).update(**request.data)
        return Response(data={'details': 'Book data are updated. '}, status=status.HTTP_200_OK)


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        product_tag = request.data.get('product_tag', None)
        product_name = request.data.get('product_name', None)
        category = request.data.get('category', None)
        category_ob = None

        if category is None:
            return Response(data={'details': 'Category name required. '}, status=status.HTTP_404_NOT_FOUND)

        # if "id" in request.data["category"]:
        if "id" in request.data["category"].keys():
            category_ob = Category.objects.filter(id=category["id"]).first()
            if not category_ob:
                return Response(data={'details': "category id doesn't exist"})
        # elif "name" in request.data["category"]:
        elif "name" in request.data["category"].keys():
            category_ob = Category.objects.filter(category_title=category["name"]).first()
            if not category_ob:
                category_ob = Category.objects.create(category_title=category["name"])

        product_price = request.data.get('product_price', None)
        stock = request.data.get('stock', None)
        image_url = request.data.get('image_url', None)
        description = request.data.get('description', None)
        product_obj = Product(product_tag=product_tag, product_name=product_name, category_id=category_ob.id,
                              product_price=product_price, stock=stock, image_url=image_url, description=description)
        product_obj.save()
        serializer = ProductSerializer(product_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # data_list = []
        #
        # for p in queryset:
        #     data_dict = {
        #         "id": p.id,
        #         "product_tag": p.product_tag,
        #         "product_name": p.product_name,
        #         "description": p.description,
        #     }
        #     data_list.append(data_dict)
        # return JsonResponse(data_list, safe=False)


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product_queryset = Product.objects.filter(pk=kwargs['pk']).first()
        if product_queryset is None:
            return Response(data={'details': 'No Product found regarding this id. '}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product_queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        # product_queryset = Product.objects.filter(id=pk).update(**request.data)
        return Response(data={'Products are updated. '}, status=status.HTTP_200_OK)

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
