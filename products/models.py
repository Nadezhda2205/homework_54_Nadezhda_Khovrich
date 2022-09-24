from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=500, null=True, blank=True)

    
    def __str__(self):
        return (self.name)


class Product(models.Model):
    name = models.TextField(verbose_name='Наименование', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=500, null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=8)
    img = models.TextField(verbose_name='Изображение', max_length=200, null=True, blank=True)


    def __str__(self):
        return (self.name)


