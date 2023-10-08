from django.urls import path
from erp.dashboard.views.views import *
from erp.dashboard.views.users_views.views import *
from erp.dashboard.views.deudas.views import *
from erp.dashboard.views.predios.views import *
urlpatterns = [
    path('Dashadmin/', IndexView.as_view(), name="home"),

    path('Users', UserView.as_view(), name="userhome"),
    path('Predio', PredioList.as_view(), name="predio"),
    path('Deuda/', DeudasView.as_view(), name="deudas"),

    path('Users/Create', NewContribuyente.as_view(), name="create"),
    path('Predio/Create', NewPredio.as_view(), name="newpredio"),
    path('Deuda/Create', NewDeuda.as_view(), name="new"),

    path('Users/Edit/<int:pk>', EditContribuyente.as_view(), name="editcontrib"),
    path('Deuda/Edit/<int:pk>', EditDeuda.as_view(), name='edit'),
    path('Predio/Edit/<int:pk>', EditPredio.as_view(), name='editpredio'),

    path('Users/Delete/<int:pk>', DeleteContribuyente.as_view(), name="delcontrib"),
]
