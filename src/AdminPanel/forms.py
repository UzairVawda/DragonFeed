from django import forms
from django.forms import ModelForm

from .models import Article

class DateInput(forms.DateInput):
    input_type = 'date'

class AddEventForm(ModelForm):

    class Meta:
        model = Article
        fields = ['Title', 'Orginization', 'Location', 'Description', 'Start', 'End', 'Tag', 'Link', 'Flyer']
        widgets = {
            'Start': DateInput(),
            'End': DateInput(),
        }