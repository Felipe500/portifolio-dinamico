from django.urls import path
from .views import ContactMeView

urlpatterns = [
    path('', ContactMeView.as_view(), name='contact_me'),
]
