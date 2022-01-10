from django.urls import path

from core.users.estudiante.views import *

urlpatterns = [
    # Cursos
    path('users/estudiantes/', EstudianteListView.as_view(), name='estudiante_list'),
    path('users/estudiantes/add/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('users/estudiantes/update/<int:pk>/', EstudianteUpdateView.as_view(), name='estudiante_update'),
]
