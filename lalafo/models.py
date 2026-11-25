from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    # media/categories

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title




class Lalafo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя Товары")
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")
                                #12000,99
    new_old = models.BooleanField(default=True, verbose_name="Бу/Новый")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lalafo', null=True, blank=True)

    class Meta:
        verbose_name = 'Лалафо'
        verbose_name_plural = 'Лалафо'

    def __str__(self):
        return self.name

