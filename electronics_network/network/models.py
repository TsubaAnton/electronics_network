from django.db import models
from django.core.validators import MinValueValidator
NULLABLE = {'blank': True, 'null': True}


class NetworkLink(models.Model):
    LEVELS = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель")
    )
    name = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.PositiveIntegerField(default=0, verbose_name='Номер дома')
    title_product = models.CharField(max_length=255, verbose_name='Название продукта', default='Название по умолчанию')
    model_product = models.CharField(max_length=255, verbose_name='Модель продукта', default='Не указано')
    release_date = models.DateTimeField(verbose_name='Дата выхода продукта на рынок')
    supplier = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.DecimalField("Задолженность перед поставщиком", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0, **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    level = models.PositiveSmallIntegerField(verbose_name='Уровень', choices=LEVELS, editable=False)

    def save(self, *args, **kwargs):
        if self.supplier:
            self.level = self.supplier.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'

