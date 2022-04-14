from django import forms

from rating.models import Rating


class RatingUpdateForm(forms.Form):
    star = forms.ChoiceField(
        choices=[(0, '---')] + list(Rating.DEGREES_EVALUATION_CHOICES),
        widget=forms.RadioSelect()
    )
