"""
URL configuration for proyectoInmobiliaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from principal import views #aunque de error, funciona

urlpatterns = [
    #esto es una forma
    #path('', include('principal.urls')),
    path('', views.catalogo, name='catalogo'),
    path('crearCliente', views.crearCliente, name='crearCliente'), #los name los hemos metido para no volver a doblar codigo en el views y acceder a la primera funcion en la otra
    path('modificarCliente', views.modificarCliente, name='modificarCliente'),
    path('borrarCliente', views.borrarCliente, name='borrarCliente'),
    path('admin/', admin.site.urls),
]

#!se añade a urlpatterns la ruta y lo que se hace con la ruta
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 