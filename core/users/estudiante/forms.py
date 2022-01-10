from django import forms
from core.user.models import User
from core.users.estudiante.models import Estudiantes
from django.forms import ModelForm
from django.contrib.auth import update_session_auth_hash
from crum import get_current_request


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'password', 'dni', 'email', 'groups', 'image', 'is_active'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese su número de cedula'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token','password','groups','is_active','username']


class RepresentanteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'password', 'dni', 'email', 'groups', 'image', 'is_active'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese su número de cedula'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token','password','groups','is_active','username']


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cedula'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = User
        fields = [
            'dni', 
            'first_name', 
            'last_name', 
            'username', 
        ]
        labels = {
            'dni': 'Cédula:',
            'first_name': 'Nombres:',
            'last_name': 'Apellidos:',
            'username': 'Usuario:',
        }
        widgets = {
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese la cédula'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese los nombres', 'pattern': '[a-zA-Z-áéíóúÁÉÍÓÚÑñ ]+', 'title': 'Ingrese nombres validos.'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese los apellidos', 'pattern': '[a-zA-Z-áéíóúÁÉÍÓÚÑñ ]+', 'title': 'Ingrese apellidos validos.'}),
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese el usuario'}),
        }
        exclude = ['password','email']


        