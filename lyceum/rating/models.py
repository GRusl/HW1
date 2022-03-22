from django.db import models


class Rating(models.Model):
    star = models.IntegerField('Оценка', choices=((1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'),
                                                  (4, 'Обожание'), (5, 'Любовь')), null=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
