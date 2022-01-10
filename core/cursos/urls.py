from django.urls import path

from core.cursos.views import *

urlpatterns = [
    # Cursos
    path('scm/cursos/', CursosListView.as_view(), name='cursos_list'),
    path('scm/cursos/add/', CursosCreateView.as_view(), name='cursos_create'),
    path('scm/cursos/update/<int:pk>/', CursosUpdateView.as_view(), name='cursos_update'),
]
