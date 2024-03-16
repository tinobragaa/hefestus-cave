from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Create a new customer message through
    the contact form.
    """

    placeholders = {
        'name': 'Name',
        'email': 'Email',
        'contact_reason': 'Order Number or Contact Reason',
    }

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_reason', 'message',)
        labels = {
            'contact_reason': 'Reason for Contact',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, placeholder_text in self.placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['placeholder'] = placeholder_text
