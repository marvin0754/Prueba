from django.db import models
from django.urls import reverse
# Create your models here.
class Pelicula(models.Model):

    titulo = models.CharField(max_length=30)
    imagen = models.CharField(max_length=60)
    year = models.DateField(null=True)
    actores = models.TextField()
    duracion = models.CharField(blank=True, null=True,max_length=8)       
    rating = models.IntegerField()
    sinopsis = models.TextField()
    genero = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("peliculas:pelicula-detail", kwargs = {'pk' :self.id })