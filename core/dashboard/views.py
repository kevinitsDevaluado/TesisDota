import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic import TemplateView
from core.user.models import User

from core.homepage.models import *
from core.security.models import Dashboard
from core.user.models import User
from core.security.models import *


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'panel.html'

    def get(self, request, *args, **kwargs):
        request.user.set_group_session()
        context = self.get_context_data()
        dashboard = Dashboard.objects.filter()
        if dashboard.exists():
            context['videos'] = Videos.objects.filter(state=True)
            context['news'] = News.objects.filter(state=True)
            
            print()
            return render(request, 'vtcpanel.html', context)
        return render(request, 'hztpanel.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Panel de administración'
        context['news'] = News.objects.filter(state=True)
        return context


@requires_csrf_token
def error_404(request, exception):
    return render(request, '404.html', {})


@requires_csrf_token
def error_500(request, exception):
    return render(request, '500.html', {})
