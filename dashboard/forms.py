from django import forms
from .models import BusinessCard

class BusinessCardForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields = ['title', 'company_name', 'location', 'email', 'phone_number', 'website']