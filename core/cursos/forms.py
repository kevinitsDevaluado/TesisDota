from django.forms import ModelForm
from django import forms

from .models import *

class CursoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nivel'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cursos
        fields = 'nivel','seccion', 'asignatura', 'descripcion'
        widgets = {
            'nivel': forms.TextInput(attrs={'placeholder': 'Ingrese el nivel'}),
            'seccion': forms.TextInput(attrs={'placeholder': 'Ingrese la sección '}),
            'asignatura': forms.TextInput(attrs={'placeholder': 'Ingrese la sección '}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Ingrese una descripción '}),
        }
        exclude = ['deletes']

