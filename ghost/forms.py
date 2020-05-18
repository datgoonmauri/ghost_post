from django import forms


class AddPost(forms.Form):
    CHOICES = (
        ('roast', 'ROAST'),
        ('boast', 'BOAST'),
    )
    category_choice = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES
        )
    text = forms.CharField(max_length=280)