from django.db import models


# Create your models here.

class Category(models.Model):
    category_title = models.CharField(max_length=200)

    class Meta:
        db_table = 'categories'


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15)
    pages = models.IntegerField()
    book_price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        # ordering = '-created_at'
        db_table = 'books'


class Product(models.Model):
    product_tag = models.CharField(max_length=20)
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.URLField()
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        # ordering = '-created_at'
        db_table = 'products'
