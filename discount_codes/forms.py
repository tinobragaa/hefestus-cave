from django import forms


class DiscountForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Discount Code',
    }), label='')
