from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('about/', index, name='about'),
    path('contact/', index, name='contact'),
]