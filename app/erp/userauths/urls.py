from django.urls import path
from erp.userauths.views import *

app_name = 'userauths'

urlpatterns = [
    path('sign-up/', register_view, name='sign-up')
]