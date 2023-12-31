from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(max_length=255, verbose_name="Электронная почта")

    def __str__(self):
        return f"Клиент: {self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название тега")

    def __str__(self):
        return f"Тег: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")

    def __str__(self):
        return f"Продукт: {self.name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Клиент")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    total_price = models.FloatField(verbose_name="Общая стоимость")

    def __str__(self):
        return f"Заказ: {self.customer} на сумму {self.total_price}"
