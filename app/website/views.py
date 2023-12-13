from django.shortcuts import render
from django.views import View

from app.common.choices import TYPE_PROJECT
from app.website.models import Website
from app.common.constants import default_website


class WebsiteView(View):
    def get(self, request):
        website = Website.objects.filter(is_active=True).first()
        if website:
            historic_academic = [d for d in website.historic if d["type"] in ["academic"]]
            historic_professional = [d for d in website.historic if d["type"] in ["professional"]]
            skills_card = website.skills_card
            skills = website.skills
        else:
            website = default_website
            historic_academic = []
            historic_professional = []
            skills_card = []
            skills = []

        return render(
            request,
            "index.html",
            {
                "website": website,
                "list_historic_academic": historic_academic,
                "list_historic_professional": historic_professional,
                "skills": skills,
                "cards_skills": skills_card,
                "type_projects": TYPE_PROJECT,
            },
        )
