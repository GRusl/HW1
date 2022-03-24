from django.db import models

from catalog.validators import MinNumWordsValidator, OccurrenceWordsValidator

from core.models import PublicationBaseModel


class Tag(PublicationBaseModel):
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(PublicationBaseModel):
    slug = models.SlugField(max_length=200, unique=True)

    weight = models.PositiveSmallIntegerField('Вес', default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(PublicationBaseModel):
    name = models.CharField('Название', max_length=150)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')

    text = models.TextField('Описание', validators=(MinNumWordsValidator(2),
                                                    OccurrenceWordsValidator(('превосходно', 'роскошно'))))

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
