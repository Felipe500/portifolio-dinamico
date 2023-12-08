from django.shortcuts import render
from django.views import View

from app.common.choices import TYPE_PROJECT
from app.website.models import Website
from app.historic.models import Historic


class WebsiteView(View):
    def get(self, request):
        website = Website.objects.filter(is_active=True).first()
        historic_academic = [d for d in website.historic if d["type"] in ["academic"]]
        historic_professional = [d for d in website.historic if d["type"] in ["professional"]]
        print(list(TYPE_PROJECT))
        for TYPE in TYPE_PROJECT:
            print(TYPE[1])

        return render(
            request,
            "index.html",
            {
                "website": website,
                "list_historic_academic": historic_academic,
                "list_historic_professional": historic_professional,
                "skills": website.skills,
                "cards_skills": website.skills_card,
                "type_projects": TYPE_PROJECT,
            },
        )
