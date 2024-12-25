from django.contrib import admin
from .models import BusinessCard

@admin.register(BusinessCard)
class BusinessCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'company_name', 'email', 'phone_number', 'website', 'created_at', 'updated_at')
    search_fields = ('title', 'first_name', 'last_name', 'company_name', 'email', 'phone_number', 'website')
    list_filter = ('company_name', 'created_at', 'updated_at')
    ordering = ('-created_at',)
