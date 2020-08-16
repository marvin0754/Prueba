"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from peliculas.views import PeliculaHomeView,PeliculaBuscar
from django.contrib.auth.decorators import login_required
from usuarios.views import Login,logoutUsuario

urlpatterns = [
    path('peliculas/', include('peliculas.urls')),
    path('admin/', admin.site.urls),
    path('', PeliculaHomeView.as_view(),name='pelicula-home'),
    #login
    path('login/',Login.as_view(), name='login'),
    path('logout/',login_required(logoutUsuario),name='logout'),
    #ajax
    path("buscar",PeliculaBuscar.as_view(),name='pelicula-buscar'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

