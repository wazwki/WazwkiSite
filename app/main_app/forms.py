''' Forms for main_app app '''

from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    ''' Form contact '''
    class Meta:
        model = Contact
        fields = ["mail", "telegram", "vacancy", "description_vacancy"]
