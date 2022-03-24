from django.db import models


class PublicationBaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    name = models.CharField('Название', max_length=150, default='', help_text='Максимальная длина - 150 символов')

    slug = models.SlugField(max_length=200, unique=True, help_text='Максимальная длина - 200 символов, уникальное '
                                                                   'значение рамках таблицы, только цифры, буквы '
                                                                   'латиницы и символы - и _')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
