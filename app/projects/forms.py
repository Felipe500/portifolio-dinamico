from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].disabled = True