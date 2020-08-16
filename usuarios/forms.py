from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from .models import Usuario

class FormaRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    class Meta:
        model = Usuario
        fields = ('correo',)

    def clean_email(self):
        correo = self.cleaned_data.get('correo')
        qs = Usuario.objects.filter(correo=correo)
        if qs.exists():
            raise forms.ValidationError('correo ya registrado')
        return correo
    def clean_password2(self):
        # Checar que contraseñas coincidan
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

class AdminFormaCreacionUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)

    class Meta:
        model =  Usuario
        fields = ('correo','nombre','apellido_paterno','apellido_materno')
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    def save(self,commit=True):
        #guardar contraseña en formato hash
        usuario= super(AdminFormaCreacionUsuario,self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario

class AdminFormaActualizar(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = Usuario
        fields = ('correo', 'password', 'apellido_paterno', 'apellido_materno', 'active', 'admin')
    
    def clean_password(self):
        return self.initial['password']





class FormularioLogin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
