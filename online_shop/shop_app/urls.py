from django.urls import path
from .views import CategoryListAPIView, CategoryRetrieveAPIView, CategoryCreateAPIView, BookListAPIView,\
    BookDetailAPIView, BookCreateAPIView

urlpatterns = [
    path('category/list/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/detail/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),

    path('book/create/', BookCreateAPIView.as_view(), name='book_create'),
    path('book/list/', BookListAPIView.as_view(), name='book_list'),
    path('book/detail/<int:pk>/', BookDetailAPIView.as_view(), name='book_detail'),
    # path('product/list/', ProductListAPIView.as_view(), name='product_list'),
    # path('product/detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
]
