from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Категорія")
    description = models.TextField(blank=True, verbose_name="Опис")

    def str(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва інструмента")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    brand = models.CharField(max_length=50, verbose_name="Бренд", default="Без бренду")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    weight = models.FloatField(verbose_name="Вага (кг)", default=1.0)
    material = models.CharField(max_length=50, verbose_name="Матеріал", default="метал")
    is_available = models.BooleanField(default=True, verbose_name="В наявності")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    def str(self):
        return f"{self.name} ({self.brand})"