from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Create a new customer message through
    the contact form.
    """
    
    # Define placeholders as class variables
    placeholders = {
        'name': 'Name',
        'email': 'Email',
        'contact_reason': 'Order Number or Contact Reason',
    }
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_reason', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Loop through placeholders defined in the class and set them as placeholders
        for field_name, placeholder_text in self.placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['placeholder'] = placeholder_text
