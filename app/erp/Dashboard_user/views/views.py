from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from erp.dashboard.models import *
from erp.mixins import IsSuperUserMixin
from erp.userauths.forms import ProfileForm
from erp.userauths.models import Profile, Predio


class ViewDashboard(LoginRequiredMixin, ListView):
    model = Predio
    template_name = 'dash_user.html'

    def get_queryset(self):
        # Obtiene el perfil del usuario actual
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            profile = None

        # Obtén todos los predios asociados al perfil (usuario)
        if profile:
            predios = Predio.objects.filter(propietario=profile)
        else:
            predios = Predio.objects.none()  # Retorna una queryset vacía si no se encuentra un perfil

        return predios

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context


def ProfileView(request):

    profile = Profile.objects.get(user=request.user)
    user = request.user  # Obtén el usuario actual
    profile, created = Profile.objects.get_or_create(user=user)
    context = {'profile':profile,}
    return render(request, 'profile.html',context )


def profile_update(request):
    user = request.user  # Obtén el usuario actual
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, initial={'email': user.email})


    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile_edit.html', context)


def list_deudas(request):
    profile = Profile.objects.get(user=request.user)

    user_profile = Profile.objects.get(user=request.user)
    deudas_pendientes = user_profile.deuda_set.filter(estado='pendiente')
    context = {
        'user_profile': user_profile,
        'deudas_pendientes': deudas_pendientes,
        'profile':profile
    }
    return render(request, 'deudas_user.html', context)


def list_historial(request):

    user_profile = Profile.objects.get(user=request.user)
    historial = user_profile.deuda_set.filter(estado='cancelado')
    context = {
        'user_profile': user_profile,
        'historial': historial,
        'profile':user_profile
    }
    return render(request, 'historial.html', context)