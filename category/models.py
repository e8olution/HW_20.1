from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
