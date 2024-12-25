from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms import BusinessCardForm
from .models import BusinessCard

@login_required
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
def edit_business_card_view(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    if request.method == 'POST':
        form = BusinessCardForm(request.POST, instance=business_card)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BusinessCardForm(instance=business_card)
    return render(request, 'dashboard/edit_business_card.html', {'form': form, 'business_card': business_card})

@login_required
def share_business_card_view(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    return render(request, 'dashboard/share_business_card.html', {
        'business_card': business_card,
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

@login_required
def delete_business_card_view(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    if request.method == 'POST':
        business_card.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_business_card.html', {'business_card': business_card})