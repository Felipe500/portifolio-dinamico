from django import forms
from .models import ContactMe


class ContactMeForm(forms.ModelForm):
    name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(label='Celular', widget=forms.TextInput(attrs={"class": "form-control"}))
    subject = forms.CharField(label='Assunto', widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": "3"
    }))

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

    class Meta:
        model = ContactMe
        fields = ['name', 'email', 'phone', 'subject', 'message']
