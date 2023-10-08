from django.urls import path
from .views.views import *

urlpatterns = [
    path('', ViewDashboard.as_view(), name='dashboard'),
    path('profile/', ProfileView, name='profile'),
    path('profile/edit', profile_update, name='profile_update'),
    path('deudas/', list_deudas, name='deudas_user'),
    path('deudas/historial', list_historial, name='historial_deudas'),
]