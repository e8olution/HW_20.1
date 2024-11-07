from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='product_images/', blank=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    manufactured_at = models.DateField(null=True, blank=True, verbose_name="Дата производства")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
