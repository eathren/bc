from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid

class BusinessCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"

    def get_absolute_url(self):
        return reverse('business_card_detail', kwargs={'uuid': self.uuid})