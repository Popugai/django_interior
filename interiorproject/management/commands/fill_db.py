# management/commands/fill_db.py
# Запускается из командной строки python manage.py fill_db

from django.core.management.base import BaseCommand

from interior.models import Product_Category, Product

from django.contrib.auth.models import User

import json, os

JSON_PATH = 'interior/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
    return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories = loadFromJSON('categories')

        Product_Category.objects.all().delete()
        for category in categories:
            new_category = Product_Category(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = Product_Category.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()
            # Создаем суперпользователя при помощи менеджера модели
        super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
