from django.contrib import admin
from .models import Category, Book, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_title']
    # fields = '__all__'


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    exclude = ['updated_at']
    # fields = '__all__'


admin.site.register(Book, BookAdmin)


class ProductAdmin(admin.ModelAdmin):
    exclude = ['updated_at']
    # fields = '__all__'


admin.site.register(Product, ProductAdmin)
