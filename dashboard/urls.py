from django.urls import path
from .views import dashboard_view, add_business_card_view, business_card_detail_view, edit_business_card_view, share_business_card_view, delete_business_card_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('add/', add_business_card_view, name='add_business_card'),
    path('card/<uuid:uuid>/', business_card_detail_view, name='business_card_detail'),
    path('card/<uuid:uuid>/edit/', edit_business_card_view, name='edit_business_card'),
    path('card/<uuid:uuid>/share/', share_business_card_view, name='share_business_card'),
    path('card/<uuid:uuid>/delete/', delete_business_card_view, name='delete_business_card'),
]