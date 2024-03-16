from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Create a new customer message through
    the contact form.
    """
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_reason', 'message',)
