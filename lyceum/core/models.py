import string

from django.db import models

from core.validators import ConsistsValidator


class TagBaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    slug = models.CharField(max_length=200, unique=True,
                            validators=(ConsistsValidator(set(string.ascii_lowercase + string.ascii_uppercase +
                                                          string.digits + "_-")), ))

    class Meta:
        abstract = True
