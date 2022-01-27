from django.forms import ModelForm
from django import forms

from .models import *

class JuegosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['autofocus'] = True

    class Meta:
        model = Juegos
        fields = 'url','name',  'description'
        widgets = {
            'url': forms.TextInput(attrs={'placeholder': 'Ingrese la url'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el Nombre del Juego '}),
            'description': forms.Textarea(attrs={'placeholder': 'Ingrese una descripción '}),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

