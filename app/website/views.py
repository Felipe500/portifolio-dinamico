from django.shortcuts import render
from django.views import View

from app.website.models import Website
from app.common.constants import default_website


class WebsiteView(View):
    def get(self, request):
        website = Website.objects.filter(is_active=True).first()

        if not website:
            website = default_website

        return render(request, "index.html", {"website": website})
