from django import forms
from .models import BusinessCard

class BusinessCardForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields = ['first_name', 'last_name', 'title', 'company_name', 'location', 'email', 'phone_number', 'website']