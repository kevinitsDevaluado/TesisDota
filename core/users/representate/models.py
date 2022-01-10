import os

from django.db import models
from django.forms import model_to_dict

from datetime import datetime

from config import settings

from core.user.models import *

class Representante(models.Model):
    nombres_re = models.CharField(max_length=150, null=True, blank=True,)
    apellidos_re = models.CharField(max_length=150, null=True, blank=True,)
    cedula = models.CharField(max_length=150, null=True, blank=True,)
    asignatura = models.CharField(max_length=150, null=True, blank=True,)
    descripcion = models.CharField(max_length=5000, null=True, blank=True,)
    deletes = models.BooleanField(default=False, verbose_name='')

    def __str__(self):
        return self.nivel

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Curso | Materia'
        verbose_name_plural = 'Cursos | Materias'
        ordering = ['-id']
