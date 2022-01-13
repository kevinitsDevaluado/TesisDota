import os

from django.db import models
from django.forms import model_to_dict

from datetime import datetime

from config import settings

from core.user.models import *
from core.cursos.models import *
from core.users.estudiante.models import *

class Matricula(models.Model):
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='',related_name='profesor')    
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, blank=True, null=True, default='',related_name='estudiante')
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, blank=True, null=True, default='')
    observacion = models.CharField(max_length=2500, verbose_name='Observación', blank=True, null=True)
    deletes = models.BooleanField(default=False, verbose_name='')


    def __str__(self):
        return self.nivel

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Matricula | Estudiante'
        verbose_name_plural = 'Matriculas | Estudiantes'
        ordering = ['-id']


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='',related_name='Usuario')    
    publicacion = models.CharField(max_length=2500, verbose_name='Publicación', blank=True, null=True)
    creada_en = models.DateTimeField(auto_now=True, null=True, blank=True)
    deletes = models.BooleanField(default=False, verbose_name='')
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, blank=True, null=True, default='',related_name='Curso')    
    

    def __str__(self):
        return self.publicacion

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Post | Publicación'
        verbose_name_plural = 'Post | Publicación'
        ordering = ['-id']

class ListaEstudiantes(models.Model):
    asistencia = models.BooleanField(default=True, verbose_name='asistencia')
    deletes = models.BooleanField(default=False, verbose_name='deletes')
    estudiant = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, blank=True, null=True, default='')    
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, blank=True, null=True, default='')    
    creada_en = models.DateTimeField(auto_now=True, null=True, blank=True)
    

    def __str__(self):
        return self.estudiantes.id

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Estudiante | Lista'
        verbose_name_plural = 'Estudiantes | Listas'
        ordering = ['-id']