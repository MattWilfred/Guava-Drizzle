from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall']