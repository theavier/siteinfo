from django import forms
from .models import Site

class AddSite(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'