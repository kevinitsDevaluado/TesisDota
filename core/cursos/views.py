import json

from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.cursos.forms import *
from core.security.mixins import PermissionMixin
from core.cursos.models import * 

from django.contrib import messages


class CursosListView(PermissionMixin, ListView):
    model = Cursos
    template_name = 'cursos/list.html'
    permission_required = 'view_cursos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curos = Cursos.objects.filter(profesor__id = self.request.user.id)
        context['create_url'] = reverse_lazy('cursos_create')
        context['title'] = 'Listado de Cursos'
        context['object_list'] = curos
        return context


class CursosCreateView(PermissionMixin, CreateView):
    model = Cursos
    template_name = 'cursos/create.html'
    form_class = CursoForm
    success_url = reverse_lazy('cursos_list')
    permission_required = 'add_cursos'

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'name':
                if Cursos.objects.filter(nivel__iexact=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        form = CursoForm(request.POST)
        try:
            if action == 'add':
                if form.is_valid():
                    form.instance.profesor_id = request.user.id
                    form.save()
                    #messages.info(request, "Grupo de Trabajo Creado Correctamente..")
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Curso'
        context['action'] = 'add'
        return context


class CursosUpdateView(PermissionMixin, UpdateView):
    model = Cursos
    template_name = 'cursos/create.html'
    form_class = CursoForm
    success_url = reverse_lazy('cursos_list')
    permission_required = 'change_cursos'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'name':
                if Cursos.objects.filter(nivel__iexact=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
            data = {}
            action = request.POST['action']
            id_cursos = self.kwargs['pk']
            cursos = Cursos.objects.get(id=id_cursos)
            form = CursoForm(request.POST, instance=cursos, files=request.FILES)
            try:
                if action == 'edit':
                    if form.is_valid():
                        #form.instance.user_creation = request.user.id
                        form.save()
                        #messages.info(request, "Grupo de Trabajo Creado Correctamente..")
                elif action == 'validate_data':
                    return self.validate_data()
                else:
                    data['error'] = 'No ha seleccionado ninguna opción'
            except Exception as e:
                data['error'] = str(e)
            return HttpResponse(json.dumps(data), content_type='application/json')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        id_Cursos = self.kwargs['pk']
        curso = Cursos.objects.get(id=id_Cursos)
        context['list_url'] = self.success_url
        context['title'] = 'Edición de un Curso'
        context['form'] = CursoForm(instance=curso)
        context['action'] = 'edit'
        return context



