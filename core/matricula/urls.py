from django.urls import path

from core.matricula.views import *

urlpatterns = [
    # Cursos
    path('scm/verCurso/<int:pk>/', VerCursoListView.as_view(), name='verCurso'),
    path('scm/cursos/', MatriculaListView.as_view(), name='matricula_list'),
    
]
