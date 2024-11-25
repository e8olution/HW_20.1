import json
from django.core.management.base import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Загружаем данные из фикстуры с категориями"""
        with open('fixtures/categories.json', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def json_read_products():
        """Загружаем данные из фикстуры с продуктами"""
        with open('fixtures/products.json', encoding='utf-8') as f:
            return json.load(f)

    def handle(self, *args, **options):
        # Удаляем все продукты и категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаём списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обрабатываем данные категорий из фикстуры
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    id=category['pk'],
                    name=category['fields']['name'],
                    description=category['fields']['description']
                )
            )

        # Создаём категории в базе данных
        Category.objects.bulk_create(category_for_create)

        # Обрабатываем данные продуктов из фикстуры
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    id=product['pk'],
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    price=product['fields']['price'],
                    category=Category.objects.get(pk=product['fields']['category']),
                    created_at=product['fields']['created_at'],
                    updated_at=product['fields']['updated_at']
                )
            )

        # Создаём продукты в базе данных
        Product.objects.bulk_create(product_for_create)
