from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from catalog.validators import MinNumWordsValidator, OccurrenceWordsValidator

from core.models import TagBaseModel


class Tag(TagBaseModel):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(TagBaseModel):
    weight = models.IntegerField('Вес', default=100, validators=(MinValueValidator(0), MaxValueValidator(32767)))

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    tags = models.ManyToManyField(Tag)

    name = models.CharField('Название', max_length=150)
    text = models.TextField('Текст', validators=(MinNumWordsValidator(2),
                                                 OccurrenceWordsValidator(('превосходно', 'роскошно'))))

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
