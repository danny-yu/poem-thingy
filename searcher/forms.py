from django import forms

class SearchForm(forms.Form):
    word = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your word here',
                'class': 'input-field'
            }
        )
    )