from django.urls import path
from .views import business_card_detail_view, dashboard_view, add_business_card_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('add/', add_business_card_view, name='add_business_card'),
    path('card/<uuid:uuid>/', business_card_detail_view, name='business_card_detail'),
]