from django.db import models
from django.db.models import Prefetch

from catalog.validators import MinNumWordsValidator, OccurrenceWordsValidator

from core.models import PublicationBaseModel, SlugBaseModel


class ItemManager(models.Manager):
    def get_for_write(self):
        return self.get_queryset().filter(
            is_published=True
        ).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.get_published())
        )


class Tag(PublicationBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(PublicationBaseModel, SlugBaseModel):
    weight = models.PositiveSmallIntegerField('Вес', default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(PublicationBaseModel):
    name = models.CharField('Название', max_length=150, help_text='Максимальная длина - 150 символов')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    text = models.TextField('Описание',
                            validators=(MinNumWordsValidator(2),
                                        OccurrenceWordsValidator(('превосходно', 'роскошно'))),
                            help_text='Минимум два слова. Обязательно содержится слово "превосходно" или "роскошно"')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    objects = ItemManager()
