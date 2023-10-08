from django.urls import path
from erp.dashboard.views.views import *
urlpatterns = [
    path('Dashadmin/', IndexView.as_view(), name="home")
]
