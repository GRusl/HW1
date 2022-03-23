from django.forms import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ConsistsValidator:
    def __init__(self, symbols: set):
        self.symbols = symbols

    def __call__(self, value):
        # The string is not reduced to lowercase due to the possibility of further uneversal use
        if set(value) - self.symbols:
            raise ValidationError(f'В тексте должны содержаться только символы: {self.symbols}')
