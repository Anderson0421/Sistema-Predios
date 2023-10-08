from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from erp.userauths.models import Deuda
from erp.usuarios.forms import DeudaForm


class DeudasView(PermissionRequiredMixin, ListView):
    permission_required = 'view_contribuyente'
    model = Deuda
    template_name = 'deudas.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Deudas'
        context['create_url'] = reverse_lazy('new')
        context['entity'] = 'Deudas'
        return context

class NewDeuda(PermissionRequiredMixin, CreateView):
    permission_required = 'view_contribuyente'
    model = Deuda
    template_name = 'new.html'
    form_class = DeudaForm
    success_url = reverse_lazy('deudas')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Deuda'
        context['entity'] = 'Deudas'
        context['create_url'] = reverse_lazy('newpredio')
        context['list_url'] = reverse_lazy('deudas')
        context['action'] = 'add'
        return context

class EditDeuda(PermissionRequiredMixin, UpdateView):
    permission_required = 'view_contribuyente'
    model = Deuda
    template_name = 'edit.html'
    form_class = DeudaForm
    success_url = reverse_lazy('deudas')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de una deuda'
        context['list_url'] = reverse_lazy('deudas')
        context['entity'] = 'Deuda'
        context['action'] = 'edit'
        return context
