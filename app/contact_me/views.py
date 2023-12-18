from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .forms import ContactMeForm


class ContactMeView(View):
    def get(self, request):
        return render(request, 'contact_me.html', {
            'form_contact_me': ContactMeForm(),
        })

    def post(self,  *args, **kwargs):
        form = ContactMeForm(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return JsonResponse({'message': 'success'})
        return render(self.request, 'contact_me.html', {
            'form_contact_me': form,
        })
