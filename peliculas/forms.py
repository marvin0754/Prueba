import datetime
from django import forms
from .models import Pelicula
#from django.contrib.admin.widgets import AdminSplitDateTime,AdminDateWidget,

class UpdatePeliculaForm(forms.ModelForm):
    class Meta:
        cur_year = datetime.datetime.today().year
        BIRTH_YEAR_CHOICES = reversed(tuple([i for i in range(cur_year - 100, cur_year+1)]))
        model = Pelicula
        fields = [
            'titulo',
            'imagen',
            'year',
            'actores',
            'duracion',   
            'rating',
            'sinopsis',
            'genero',
        ]
        widgets = {
            'year': forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), 
        }
          #'duracion' : forms.TimeField(attrs={'class':'timepicker'}),
class CreatePeliculaForm(forms.ModelForm):
    class Meta:
        cur_year2 = datetime.datetime.today().year
        BIRTH_YEAR_CHOICES2 = reversed(tuple([i for i in range(cur_year2 - 100, cur_year2 )]))
        model = Pelicula
        fields = [
            'titulo',
            'imagen',
            'year',
            'actores',
            'duracion',   
            'rating',
            'sinopsis',
            'genero',
        ]
        widgets = {
            'year': forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES2),
        }

    #def __init__(self, *args, **kwargs):
        #super(CreatePeliculaForm    , self).__init__(*args, **kwargs)
        #self.fields['duracion'].widget = widgets.AdminTimeWidget()
#class CustomAdminSplitDateTime(AdminSplitDateTime):
    #def __init__(self, attrs=None):
        #widgets = [AdminDateWidget, AdminTimeWidget(attrs=None, format='%I:%M %p')]
        #forms.MultiWidget.__init__(self, widgets, attrs)
    
