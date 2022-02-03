import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.homepage.forms import TareasEnviadas, TareasDirigidasForm
from core.security.mixins import PermissionMixin


class TareasDirigidasListView(PermissionMixin, ListView):
    model = TareasEnviadas
    template_name = 'tareasDirigidas/list.html'
    permission_required = 'view_tareasenviadas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('tareasDirigidas_create')
        context['title'] = 'Listado de Tareas Dirigidas|'
        return context


class TareasDirigidasCreateView(PermissionMixin, CreateView):
    model = TareasEnviadas
    template_name = 'tareasDirigidas/create.html'
    form_class = TareasDirigidasForm
    success_url = reverse_lazy('tareasDirigidas_list')
    permission_required = 'add_tareasenviadas'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de una Tarea Dirigida'
        context['action'] = 'add'
        return context


class TareasDirigidasUpdateView(PermissionMixin, UpdateView):
    model = TareasEnviadas
    template_name = 'tareasDirigidas/create.html'
    form_class = TareasDirigidasForm
    success_url = reverse_lazy('tareasDirigidas_list')
    permission_required = 'change_tareasenviadas'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'edit':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Edición de una Tarea Dirigida'
        context['action'] = 'edit'
        return context


class TareasDirigidasDeleteView(PermissionMixin, DeleteView):
    model = TareasEnviadas
    template_name = 'tareasDirigidas/delete.html'
    success_url = reverse_lazy('tareasDirigidas_list')
    permission_required = 'delete_tareasenviadas'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notificación de eliminación'
        context['list_url'] = self.success_url
        return context
