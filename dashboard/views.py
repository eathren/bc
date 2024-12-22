from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms import BusinessCardForm
from .models import BusinessCard

def business_card_detail_view(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    return render(request, 'dashboard/business_card_detail.html', {'business_card': business_card})

@login_required
def dashboard_view(request):
    business_cards = BusinessCard.objects.filter(user=request.user)
    can_add_card = business_cards.count() < 3
    return render(request, 'dashboard/dashboard.html', {
        'business_cards': business_cards,
        'can_add_card': can_add_card
    })
    
@login_required
def add_business_card_view(request):
    if request.method == 'POST':
        form = BusinessCardForm(request.POST)
        if form.is_valid():
            business_card = form.save(commit=False)
            business_card.user = request.user
            business_card.save()
            return redirect('dashboard')
    else:
        form = BusinessCardForm()
    return render(request, 'dashboard/add_business_card.html', {'form': form})