from django import forms
from .models import Car


class form_cars(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'