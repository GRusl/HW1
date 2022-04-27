import re

from django.forms import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinNumWordsValidator:
    def __init__(self, num: int):
        self.num = num

    def __call__(self, value):
        if len(re.sub(r"</?[a-z]+>", "", value).split()) < self.num:
            raise ValidationError(f"Напишити, как минимум, {self.num} слов(а)")


@deconstructible
class OccurrenceWordsValidator:
    def __init__(self, words):
        self.words = set(map(lambda x: x.lower(), words))

    def __call__(self, value):
        if not set(re.sub(r"</?[a-z]+>", "", value).lower().split()) & self.words:
            raise ValidationError(
                f'Используйте такие слова, как: {", ".join(self.words)}'
            )
