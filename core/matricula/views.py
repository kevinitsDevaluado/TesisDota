import json

from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView
from django.db import transaction
from django.db.models import Q

from core.matricula.forms import *
from core.security.mixins import PermissionMixin
from core.matricula.models import * 
from core.homepage.models import *
from django.contrib import messages
from django.shortcuts import render, redirect

from core.cursos.models import *
from crum import get_current_user

class VerCursoListView(CreateView):
    template_name = 'matricula/verCurso.html'
    form_class = MatriculaForm


    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('verCurso', kwargs={'pk': pk})

    def validate_data(self):
            data = {'valid': True}
            try:
                type = self.request.POST['type']
                obj = self.request.POST['obj'].strip()
                pk = self.kwargs['pk']

                if type == 'estudiante':
                    if Matricula.objects.filter(estudiante_id=obj,curso_id=pk):
                        data['valid'] = False
                elif type == 'name':
                    if CrearTarea.objects.filter(name__icontains=obj,curso_id=pk):
                        data['valid'] = False
            except:
                pass
            return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        action = request.POST['action']
        data = {}
        try:
            if action == 'add':
                with transaction.atomic():
                    print('Accion Agregar Matricula',action)
                    estudiante = request.POST['estudiante']
                    print('estudiante',estudiante)
                    observacion = request.POST['observacion']
                    print('observacion',observacion)
                    curso = self.kwargs['pk']
                    e = Matricula()
                    e.estudiante_id = estudiante
                    e.curso_id = curso
                    e.profesor_id = request.user.id
                    e.observacion = observacion
                    e.save()    
            elif action == 'post_add':
                with transaction.atomic():
                    print('Accion Agregar Foro',action)
                    message = request.POST['publicacion']
                    print('mensaje de la publicacion: ',message)
                    curso_id = self.kwargs['pk']
                    pb = Post()
                    pb.publicacion = message
                    pb.curso_id = curso_id
                    pb.user_id = request.user.id
                    pb.save()
            elif action == 'add_list':
                with transaction.atomic():
                    check = request.POST.getlist('checks[]')                    
                    for i in check:
                        lista = ListaEstudiantes ()
                        lista.estudiant_id = i
                        lista.curso_id = self.kwargs['pk']
                        lista.asistencia = False
                        lista.save()
            elif action == 'add_homework':
                with transaction.atomic():
                    id_curso = self.kwargs['pk']
                    estudiants = Matricula.objects.filter(curso=id_curso)
                    tema = request.POST['name']
                    #print('tema: ',tema)
                    juego = request.POST['juego']
                    #print('juego: ',juego)
                    descripcion = request.POST['descripcion']
                    #print('descripcion: ', descripcion)
                    crear = CrearTarea()
                    crear.name = tema
                    crear.curso_id = id_curso
                    crear.juego_id = juego
                    crear.descripcion = descripcion
                    crear.save()
                    tareaActual = CrearTarea.objects.get(name__icontains = tema)
                    #print('Tarea Actual: ',tareaActual.id)
                    if tareaActual :               
                        for i in estudiants:
                            print('Tarea Actual: ', tareaActual.id)
                            print('estudiante: ', i.estudiante_id)
                            entregar = EntregarTarea()
                            entregar.tarea_id = tareaActual.id
                            entregar.estudiante_id = i.estudiante_id
                            entregar.save()
            elif action == 'update_nota':
                with transaction.atomic():
                    nota = request.POST['nota']
                    print('id tarea: ',nota)
                    tarea = request.POST['id_tarea']
                    estudiante = request.POST['id_estudiante']
                    print('estudiante_id', estudiante)
                    print('id tarea', tarea)
                    km = EntregarTarea.objects.get(tarea_id = tarea,estudiante_id = estudiante)
                    km.nota = nota
                    km.save()
                   
                                                        
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        
        id_curso = self.kwargs['pk']
        
        curso = Cursos.objects.get(id=id_curso)
        info = Mainpage.objects.get(id=1)
        matriculados = Matricula.objects.filter(curso=id_curso)
        asistencias = ListaEstudiantes.objects.filter(curso=id_curso)
        tareas = EntregarTarea.objects.filter(tarea__curso=id_curso)
        tareasIndividual = EntregarTarea.objects.filter(tarea__curso=id_curso, estudiante__user__id = self.request.user.id)
        asistenciasIndividuales = ListaEstudiantes.objects.filter(curso=id_curso, estudiant__user__id = self.request.user.id)

        #SELECT *FROM MATRICULA where id_curso = 1;
        #matriculados = Matricula.objects.filter(curso=id_curso)

        count = Matricula.objects.filter(curso=id_curso).count
        context['title'] = 'La educación es el camino, no el objetivo.'
        context['curso'] = curso    
        context['titulo'] = 'Matrículas'
        context['list_url'] = reverse_lazy('verCurso', kwargs={'pk': self.kwargs['pk']})
        context['action'] = 'add'
        context['info'] = info
        context['user'] = self.request.user.username
        context['deberes'] = 'Deberes'
        context['asistenciaList'] = 'Deberes'
        context['post'] = Post.objects.filter(curso=id_curso)
        context['formPost'] = PostForm()
        context['form'] = MatriculaForm()
        context['asistencias'] = asistencias
        context['matricula'] = matriculados
        context['formAsistencia'] = AsistenciaForm
        context['cursos'] =  id_curso
        context['count'] = count
        context['formCrearTarea'] = CrearTareaForm()
        context['tareas'] = tareas
        context['tareasIndividual'] = tareasIndividual
        context['asistenciaIndividual'] = asistenciasIndividuales

        context['tareaForm'] = TareaForm()

        
        return context


class MatriculaListView(PermissionMixin, ListView):
    model = Matricula
    template_name = 'matricula/list.html'
    permission_required = 'view_matricula'


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.request.user.id
        print(str(id_user))
        matriculados = Matricula.objects.filter(estudiante__user__id=id_user)
        context['create_url'] = reverse_lazy('cursos_create')
        context['title'] = 'Listado de Matriculas'
        context['object_list'] = matriculados
        return context



