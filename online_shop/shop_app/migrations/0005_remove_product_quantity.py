# Generated by Django 4.1.5 on 2023-01-04 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_alter_book_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
