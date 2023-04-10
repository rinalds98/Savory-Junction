from .models import Review
from django import forms

STAR_CHOICES = (
    (1, ""),
    (2, ""),
    (3, ""),
    (4, ""),
    (5, ""),
)


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=STAR_CHOICES, widget=forms.RadioSelect(attrs={"class": "icon"})
    )

    class Meta:
        model = Review
        fields = ["comment", "rating"]
