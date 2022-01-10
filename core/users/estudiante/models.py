from django.db import models
from core.user.models import User
from django.forms import model_to_dict

from crum import get_current_request

from config.settings import MEDIA_URL, STATIC_URL
from core.cursos.models import *
# Create your models here.
class Estudiantes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    representante = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, default='',related_name='representante')
    

    def __str__(self):
        return self.user.get_full_name()  
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['user'])
        item['user'] = self.user.toJSON()
        item['representante'] = self.representante.toJSON()
        return item
    

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['id']
