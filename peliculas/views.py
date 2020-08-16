from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import UpdatePeliculaForm,CreatePeliculaForm
from .models import Pelicula
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
class PeliculaListView(ListView):
    model=Pelicula

class PeliculaDetailView(DetailView):
    model =     Pelicula

class PeliculaCreateView(CreateView):
    model = Pelicula
    form_class = CreatePeliculaForm
    
class PeliculaUpdateView(UpdateView):
    model = Pelicula
    form_class = UpdatePeliculaForm
    template_name='peliculas/pelicula_update.html'
    
    
class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name='peliculas/pelicula_delete.html'
    success_url = reverse_lazy('peliculas:pelicula-list')

class PeliculaHomeView(ListView):
    model = Pelicula
    template_name='peliculas/pelicula_home.html'

class PeliculaBuscar(View):

    def get(self,request,*args,**kwards):
        val =request.GET.get('keyword') or None
        if val == None:
            #return redirect('pelicula-home')
            return HttpResponse("no HAY PARAMETROS")
        else:
            val=val.upper()
            queryset=Pelicula.objects.filter(titulo__icontains=val) #retornaObjetos Pelicula//Eq SQL:Select * from where titulo like %val%
            return JsonResponse(list(queryset.values()),safe=False)
        
      
      