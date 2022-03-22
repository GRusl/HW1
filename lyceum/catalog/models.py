import string

from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from catalog.validators import MinNumWordsValidator, OccurrenceWordsValidator
from lyceum.validators import ConsistsValidator


class TagBaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    slug = models.CharField(max_length=200, unique=True,
                            validators=(ConsistsValidator(set(string.ascii_lowercase + string.ascii_uppercase +
                                                          string.digits + "_-")), ))

    class Meta:
        abstract = True


class Item(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    name = models.CharField('Название', max_length=150)
    text = models.TextField('Текст', validators=(MinNumWordsValidator(2),
                                                 OccurrenceWordsValidator(('превосходно', 'роскошно'))))


class Tag(TagBaseModel):
    pass


class Category(TagBaseModel):
    weight = models.IntegerField('Вес', default=100, validators=(MinValueValidator(0), MaxValueValidator(32767)))
