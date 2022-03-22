import string

from django.db import models

from catalog.validators import MinNumWordsValidator, OccurrenceWordsValidator
from lyceum.validators import ConsistsValidator


class Item(models.Model):
    name = models.CharField('Название', max_length=150)
    text = models.TextField('Текст', validators=(MinNumWordsValidator(2),
                                                 OccurrenceWordsValidator(('превосходно', 'роскошно'))))

    is_published = models.BooleanField('Опубликовано', default=True)


class Tag(models.Model):
    slug = models.CharField(max_length=200, unique=True,
                            validators=(ConsistsValidator(set(string.ascii_lowercase + string.ascii_uppercase +
                                                          string.digits + "_-")), ))

    is_published = models.BooleanField('Опубликовано', default=True)
