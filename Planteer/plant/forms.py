# plants/forms.py

from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'category', 'is_edible', 'description', 'image']

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(required=False)