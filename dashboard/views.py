from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BusinessCard, Lead
from .forms import BusinessCardForm

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

def capture_lead(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        Lead.objects.create(
            business_card=business_card,
            user=business_card.user,
            name=name,
            email=email,
            phone_number=phone_number
        )
        messages.success(request, 'Your contact info has been submitted.')
        return redirect('business_card_detail', uuid=uuid)
    return render(request, 'dashboard/share_business_card.html', {'business_card': business_card})

@login_required
def add_business_card_view(request):
    if request.method == 'POST':
        form = BusinessCardForm(request.POST, request.FILES)
        if form.is_valid():
            business_card = form.save(commit=False)
            business_card.user = request.user
            business_card.save()
            messages.success(request, 'Business card added successfully.')
            return redirect('dashboard')
    else:
        form = BusinessCardForm()
    return render(request, 'dashboard/add_business_card.html', {'form': form})

@login_required
def edit_business_card_view(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    if request.method == 'POST':
        form = BusinessCardForm(request.POST, request.FILES, instance=business_card)
        if form.is_valid():
            form.save()
            messages.success(request, 'Business card updated successfully.')
            return redirect('dashboard')
    else:
        form = BusinessCardForm(instance=business_card)
    return render(request, 'dashboard/edit_business_card.html', {'form': form, 'business_card': business_card})

@login_required
def share_business_card_view(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    absolute_url = request.build_absolute_uri(business_card.get_absolute_url())
    if business_card.allow_lead_capture:
        absolute_url += '?capture_lead=true'
    return render(request, 'dashboard/share_business_card.html', {'business_card': business_card, 'absolute_url': absolute_url})

@login_required
def delete_business_card_view(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    if request.method == 'POST':
        business_card.delete()
        messages.success(request, 'Business card deleted successfully.')
        return redirect('dashboard')
    return render(request, 'dashboard/delete_business_card.html', {'business_card': business_card})


@login_required
def dashboard_view(request):
    business_cards = BusinessCard.objects.filter(user=request.user).prefetch_related('leads')
    can_add_card = business_cards.count() < 3
    return render(request, 'dashboard/dashboard.html', {
        'business_cards': business_cards,
        'can_add_card': can_add_card
    })

@login_required
def view_leads(request, uuid):
    business_card = get_object_or_404(BusinessCard, uuid=uuid, user=request.user)
    leads = business_card.leads.all()

    # Search functionality
    query = request.GET.get('q', '')
    if query:
        leads = leads.filter(Q(name__icontains=query) | Q(email__icontains=query))

    return render(request, 'dashboard/view_leads.html', {
        'business_card': business_card,
        'leads': leads,
        'query': query,
    })