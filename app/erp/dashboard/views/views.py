from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView

from erp.userauths.models import Predio, Profile


class IndexView(PermissionRequiredMixin, TemplateView):
    permission_required = 'view_contribuyente'
    template_name = 'dashboard.html'



    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['predio_count'] = Predio.objects.count()
        context['perfil_count'] = Profile.objects.count()
        return context
