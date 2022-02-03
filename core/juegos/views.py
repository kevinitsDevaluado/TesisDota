import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic import TemplateView
from core.user.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse

from core.homepage.models import *
from core.security.models import Dashboard
from core.user.models import User
from core.security.models import *
from core.juegos.models import *
from core.juegos.forms import JuegosForm
from django.urls import reverse_lazy

from core.security.mixins import PermissionMixin


class JuegoListView(PermissionMixin, ListView):
    model = Juegos
    template_name = 'juegos/list.html'
    permission_required = 'view_juegos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('juego_create')
        context['title'] = 'Listado de Juegos'
        return context


class JuegoCreateView(PermissionMixin, CreateView):
    model = Juegos
    template_name = 'juegos/create.html'
    form_class = JuegosForm
    success_url = reverse_lazy('juego_list')
    permission_required = 'add_juegos'

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'name':
                if Juegos.objects.filter(nivel__iexact=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()

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
        context['title'] = 'Nuevo registro de un Juego'
        context['action'] = 'add'
        return context


class JuegoUpdateView(PermissionMixin, UpdateView):
    model = Juegos
    template_name = 'cursos/create.html'
    form_class = JuegosForm
    success_url = reverse_lazy('juego_list')
    permission_required = 'change_juegos'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'name':
                if Juegos.objects.filter(name__iexact=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
            data = {}
            action = request.POST['action']
            id_cursos = self.kwargs['pk']
          
            try:
                if action == 'edit':
                    form = self.get_form()
                    data = form.save()
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
        context['list_url'] = self.success_url
        context['title'] = 'Edición de un JUego'
        context['action'] = 'edit'
        return context








class GameMemoryView( TemplateView):
    template_name = 'memoria/memoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Juego de Memoría'
        return context


class EncuentraElTesoroView(TemplateView):
    template_name = 'encuentraTesoro/tesoro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Encuentra el Tesoro'
        return context

class PaintView( TemplateView):
    template_name = 'paint/paint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Paint'
        return context


class RompecabezasView(TemplateView):
    template_name = 'rompecabezas/rompecabezas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rompecabezas'
        return context

class ReflejosView(TemplateView):
    template_name = 'reflejos/reflejos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reflejos'
        return context


class SentidosView(TemplateView):
    template_name = 'sentidos/sentidos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sentidos del CUerpo HUmano'
        return context


class JuegoNUevoView(TemplateView):
    template_name = 'rompecabezasnorte/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sentidos del CUerpo HUmano'
        return context