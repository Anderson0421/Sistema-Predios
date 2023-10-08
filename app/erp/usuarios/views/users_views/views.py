from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from erp.userauths.forms import ProfileForm
from erp.userauths.models import Deuda, Profile, User
from erp.dashboard.models import *


class UserView(PermissionRequiredMixin, ListView):
    permission_required = 'view_contribuyente'
    model = Profile
    template_name = 'users.html'

    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de contribuyentes'
        context['list_url'] = reverse_lazy('userhome')
        context['create_url'] = reverse_lazy('create')
        context['users'] = User.objects.all()

        context['entity'] = 'Usuarios'
        return context


class NewContribuyente(PermissionRequiredMixin, CreateView):
    permission_required = 'view_contribuyente'
    model = Profile
    form_class = ProfileForm
    template_name = 'new.html'
    success_url = reverse_lazy('userhome')


    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return render(request, self.template_name, context)


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de un nuevo Contribuyente'
        context['list_url'] = reverse_lazy('userhome')
        context['entity'] = 'Usuarios'
        context['action'] = 'add'
        return context

class EditContribuyente(PermissionRequiredMixin, UpdateView):
    permission_required = 'view_contribuyente'
    model = Profile
    form_class = ProfileForm
    template_name = 'edit.html'
    success_url = reverse_lazy('userhome')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de un nuevo Contribuyente'
        context['list_url'] = reverse_lazy('userhome')
        context['entity'] = 'Usuarios'
        context['action'] = 'edit'
        return context

class DeleteContribuyente(DeleteView):
    model = Profile
    template_name = 'delete.html'
    success_url = reverse_lazy('userhome')  # Redirección exitosa después de la eliminación

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Contribuyente'
        context['list_url'] = reverse_lazy('userhome')
        context['entity'] = 'Usuarios'
        context['action'] = 'del'
        return context
