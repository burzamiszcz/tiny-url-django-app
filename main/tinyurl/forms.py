from django import forms
from .models import Urls

class UrlForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ('main_url',)
        labels = {'main_url': 'Type URL to shorten'}
