from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from erp.userauths.models import Predio
from erp.usuarios.forms import PredioForm
from erp.dashboard.models import *


class PredioList(PermissionRequiredMixin, ListView):
    permission_required = 'view_contribuyente'
    model = Predio
    template_name = 'predios.html'

    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de predios'
        context['create_url'] = reverse_lazy('newpredio')
        context['entity'] = 'Predios'
        context['action'] = 'add'
        return context


class NewPredio(PermissionRequiredMixin, CreateView):
    permission_required = 'view_contribuyente'
    model = Predio
    template_name = 'new.html'
    form_class = PredioForm
    success_url = reverse_lazy('predio')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de predios'
        context['list_url'] = reverse_lazy('predio')
        context['entity'] = 'Predios'
        context['action'] = 'add'
        return context


class EditPredio(PermissionRequiredMixin, UpdateView):
    permission_required = 'view_contribuyente'
    model = Predio
    template_name = 'edit.html'
    form_class = PredioForm
    success_url = reverse_lazy('predio')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de un nuevo Contribuyente'
        context['list_url'] = reverse_lazy('userhome')
        context['entity'] = 'Usuarios'
        context['action'] = 'edit'
        return context
