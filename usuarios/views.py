from django.shortcuts import render
from django.urls import reverse_lazy 
from django.http import HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import login,logout

from django.views.generic.edit import FormView
from .forms import FormularioLogin
# Create your views here.


class Login(FormView):
    template_name='usuarios/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('pelicula-home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwrags):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwrags)
    
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/login/')
