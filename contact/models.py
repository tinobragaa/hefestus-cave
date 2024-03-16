from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Created when a user submits a form on the contact page.
    """

    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_reason = models.CharField(max_length=100)
    message = models.TextField(null=False, blank=False)
    date_submmited = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'Contact {self.name} and message created'
