from django.forms import ModelForm
from django import forms

from .models import *
from core.deberes.models import *
class MatriculaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['estudiante'].widget.attrs['autofocus'] = True

    class Meta:
        model = Matricula
        fields = 'estudiante','observacion'
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'select2' ,'style': 'width:100%'}),
            'observacion': forms.Textarea(attrs={'placeholder': 'Ingrese una observacion','class': 'form-control',}),
        }
        exclude = ['deletes']

class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['estudiante'].widget.attrs['autofocus'] = True
    class Meta:
        model = Post
        fields = 'publicacion',
        widgets = {
            'publicacion': forms.TextInput(attrs={'placeholder': '¿Qué estás pensando?','class': 'form-control',}),
        }
        exclude = ['deletes']



class AsistenciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['estudiante'].widget.attrs['autofocus'] = True

    class Meta:
        model = ListaEstudiantes
        fields = 'asistencia',
        widgets = {
            'asistencia': forms.CheckboxInput(attrs={'class': 'form-control-checkbox'})
        }
        exclude = ['deletes']

class CrearTareaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['estudiante'].widget.attrs['autofocus'] = True

    class Meta:
        model = CrearTarea
        fields = 'name','juego','descripcion'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el tema de la Tarea','class': 'form-control',}),
            'juego': forms.Select(attrs={'class': 'select2' ,'style': 'width:100%'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Ingrese la descripción','class': 'form-control',}),

        }


class TareaForm(ModelForm):
    
    class Meta:
        model = EntregarTarea
        fields = 'nota',
        widgets = {
            'nota': forms.Select(attrs={'class': 'select2' ,'style': 'width:100%'}),
        }
        exclude = ['tarea','estudiante']
