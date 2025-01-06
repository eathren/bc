from django import forms
from .models import BusinessCard

class BusinessCardForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields = [
            'first_name', 'last_name', 'title', 'company_name', 'location',
            'email', 'phone_number', 'website', 'icon_color', 'background_color',  'allow_lead_capture'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            'title': forms.TextInput(attrs={'class': 'input'}),
            'company_name': forms.TextInput(attrs={'class': 'input'}),
            'location': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'phone_number': forms.TextInput(attrs={'class': 'input'}),
            'website': forms.URLInput(attrs={'class': 'input'}),
            'icon_color': forms.TextInput(attrs={'type': 'color', 'class': 'input'}),
            'background_color': forms.TextInput(attrs={'type': 'color', 'class': 'input'}),
            # 'logo': forms.ClearableFileInput(attrs={'class': 'file-input'}),
            'allow_lead_capture': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }