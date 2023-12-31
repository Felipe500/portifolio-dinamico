from django.views.generic import ListView
from .models import Project


class ProjectListView(ListView):
    paginate_by = 3
    model = Project
    fields = '__all__'
    template_name = 'projects.html'
    form_filter = None

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return self.model.objects.filter(title__name__unaccent__icontains=query)
        return self.model.objects.get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        self.request.session['query'] = self.request.GET.get('query', None)
        paginator = self.paginator_class(self.get_queryset(), self.paginate_by)

        context['projects'] = paginator.page(page)
        return context

