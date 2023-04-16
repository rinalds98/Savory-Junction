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
    """
    This Class is responsible for creating the form on the review section
    of the homepage.
    """

    rating = forms.ChoiceField(
        choices=STAR_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                "class": "icon",
                "aria-label": "star-rating",
            }
        ),
    )

    class Meta:
        model = Review
        fields = ["comment", "rating"]
