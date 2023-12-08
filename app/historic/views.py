from django.views import View
from django.shortcuts import render

from .models import Historic


class ViewClient(View):
    def get(self, request):
        historics = Historic.objects.all()
        return render(request, "historic/historic.html", {"historics": historics})
