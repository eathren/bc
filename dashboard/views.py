from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import BusinessCard

@login_required
def dashboard_view(request):
    business_cards = BusinessCard.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {'business_cards': business_cards})