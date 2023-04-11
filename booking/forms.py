from .models import Review
from django import forms

STAR_CHOICES = (
    (5, ""),
    (4, ""),
    (3, ""),
    (2, ""),
    (1, ""),
)


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=STAR_CHOICES, widget=forms.RadioSelect(attrs={"class": "icon"})
    )

    class Meta:
        model = Review
        fields = ["comment", "rating"]
