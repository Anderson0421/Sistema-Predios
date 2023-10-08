
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from erp.login.views import ViewLogin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('erp.Dashboard_user.urls')),
    path('', include('erp.dashboard.urls')),
    path('', include('erp.usuarios.urls')),
    path('', include('erp.userauths.urls')),

    path('login/', ViewLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)