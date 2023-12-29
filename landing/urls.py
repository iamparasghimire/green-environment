from django.urls import path
from .views import contact_subscribe

urlpatterns = [
    path('', contact_subscribe, name='contact_subscribe'),
    # Add other URL patterns as needed
]
