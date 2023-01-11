from django.urls import path

from . import views
from .views import CategoryListAPIView, CategoryRetrieveAPIView, CategoryCreateAPIView, BookListAPIView,\
    BookDetailAPIView, BookCreateAPIView, ProductListAPIView, ProductRetrieveAPIView,ProductCreateAPIView, \
    ProductUpdateAPIView, CategoryUpdateAPIView, BookUpdateAPIView
from .views import *
urlpatterns = [
    path('category/list/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/detail/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category_update'),

    path('book/create/', BookCreateAPIView.as_view(), name='book_create'),
    path('book/list/', BookListAPIView.as_view(), name='book_list'),
    path('book/detail/<int:pk>/', BookDetailAPIView.as_view(), name='book_detail'),
    path('book/update/<int:pk>/', BookUpdateAPIView.as_view(), name='book_detail'),

    path('product/list/', ProductListAPIView.as_view(), name='product_list'),
    path('product/detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_detail'),

    path('show/data/', views.json_response, name='json_response'),
]
