from django.db import models

from catalog.models import Item

from django.contrib.auth import get_user_model


class Rating(models.Model):
    DEGREES_EVALUATION_CHOICES = (
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь')
    )

    item = models.ForeignKey(Item, on_delete=models.PROTECT, verbose_name='Товар')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='Пользователь')
    star = models.IntegerField('Оценка', choices=DEGREES_EVALUATION_CHOICES, null=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

        constraints = (
            models.UniqueConstraint(fields=['user', 'item'], name='unique appversion'),
        )
