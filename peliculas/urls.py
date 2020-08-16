from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import(
    PeliculaListView,
    PeliculaDetailView,
    PeliculaCreateView,
    PeliculaUpdateView,
    PeliculaDeleteView,
    
) 
from django.contrib.auth.decorators import login_required

app_name='peliculas'

urlpatterns=[
    path("",login_required(PeliculaListView.as_view()),name='pelicula-list'),
    path("<int:pk>/",login_required(PeliculaDetailView.as_view()),name='pelicula-detail'),
    path("create/",login_required(PeliculaCreateView.as_view()),name='pelicula-create'),
    path("<int:pk>/update/",login_required(PeliculaUpdateView.as_view()),name='pelicula-update'),
    path("<int:pk>/delete/",login_required(PeliculaDeleteView.as_view()),name='pelicula-delete'),   
]