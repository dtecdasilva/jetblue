from django.db import models
from .utils import create_new_ref_number
from django.core.mail import send_mail


class Package(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    shipped_from = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    shipped_id = models.CharField(max_length=255, default=create_new_ref_number, blank=True, editable=False, unique=True,)
    shipped = 'shipped'
    delivered = 'delivered'
    pending = 'pending'
    STATUS_CHOICES = [
        (shipped, 'shipped'),
        (delivered, 'delivered'),
        (pending, 'pending'),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=pending)




