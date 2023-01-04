from django.db import models


# Create your models here.

class Category(models.Model):
    category_title = models.CharField(max_length=200)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category_title


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15)
    author_name = models.CharField(max_length=150, blank=True)
    pages = models.IntegerField()
    book_price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'books'

    def __str__(self):
        return '{0} {1}'.format(self.book_title, self.author_name)


class Product(models.Model):
    product_tag = models.CharField(max_length=20)
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.URLField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'products'

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.product_name)
