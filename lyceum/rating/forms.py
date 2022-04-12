from django import forms

from rating.models import Rating


class RatingUpdateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = (Rating.star.field.name, )
