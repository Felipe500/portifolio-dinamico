from django.urls import path
from .views import WebsiteView


urlpatterns = [
    path("", WebsiteView.as_view(), name="index"),
]
