from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from AppWeb.models import Avatar, Empleado

class FormularioEmpleado(forms.ModelForm):  # Cambia a ModelForm
    
    class Meta:
        model = Empleado  # Especifica el modelo asociado
        fields = ['nombre', 'apellido', 'puesto']  # Lista los campos que quieres incluir en el formulario
    

    


class FormularioConsultas(forms.Form):
    usuario = forms.CharField(max_length=30)
    titulo = forms.CharField(max_length=100)
    fecha = forms.DateField()
    descripcion = forms.CharField(max_length=1000)



class FormularioDepartamento(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=300)
    
class FormularioEventos(forms.Form):
    
    nombre = forms.CharField(max_length=300)
    descripcion = forms.CharField(max_length=300)
    fecha = forms.DateField()
    
    
class UsuarioRegistro(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        
        
class FormularioEditar(UserCreationForm):
    
        
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ["imagen"]
