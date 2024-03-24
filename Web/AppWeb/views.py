from django.shortcuts import render, get_object_or_404
from AppWeb.models import *
from AppWeb.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def acercaDeMi(request):
    
    return render(request, 'AppWeb/acercaDeMi.html')

def inicio(request):
    
    return render(request, 'AppWeb/inicio.html', {"Bienvenida":"Bienvenido a mi página."})


def confirmacion_guardar(request):
    
   return render(request, 'AppWeb/confirmacion_guardar.html')

def consultas(request):

    if request.method == "POST":

        formulario = FormularioConsultas(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            consulta_nueva = Consultas(
                usuario=info_dic["usuario"],
                titulo=info_dic["titulo"],
                fecha=info_dic["fecha"],
                descripcion=info_dic["descripcion"],
                
                
                )
            
            consulta_nueva.save()
            
            return render(request, "AppWeb/confirmacion_guardar.html")
        
    else:
            
        formulario = FormularioConsultas()
    
    
    
    return render(request, 'AppWeb/consulta_nueva.html', {'formu': formulario})

def leerConsultas(request):
    
    consultas = Consultas.objects.all()
    
    contexto = {"gente":consultas}
    
    return render(request, "AppWeb/verConsultas.html", contexto)
    

@login_required
def empleado_nuevo(request):
    
    if request.method == "POST":

        formulario = FormularioEmpleado(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            empleado_nuevo = Empleado(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                puesto=info_dic["puesto"],
                
                )
            
            empleado_nuevo.save()
            
            return render(request, "AppWeb/confirmacion_guardar.html")
        
    else:
            
        formulario = FormularioEmpleado()
    
    
    
    return render(request, 'AppWeb/empleado_nuevo.html', {'formu': formulario})



def buscar_empleado(request):
    
    return render(request, "AppWeb/buscar_empleado.html")


def resultado_empleado(request):
    
    empleado = request.GET["empleado"]
    
    resultados = Empleado.objects.filter(nombre__iexact=empleado)
    
    return render(request, 'AppWeb/resultado_empleado.html', {'resultados':resultados})

def LeerEmpleados(request):
    
    empleados = Empleado.objects.all()
    
    contexto = {"trabajadores" : empleados}
    
    
    return render(request, "AppWeb/empleado.html", contexto)



def eliminarEmpleado(request, empleadoNombre):
    # Verificar si se ha enviado una solicitud POST
    if request.method == 'POST':
        # Obtener el ID del empleado que se va a eliminar
        empleado_id = request.POST.get('empleado_id')
        # Obtener el empleado específico por su ID
        empleado = get_object_or_404(Empleado, id=empleado_id)
        # Eliminar el empleado
        empleado.delete()
    
    # Obtener nuevamente la lista de empleados después de la eliminación
    empleados_actualizados = Empleado.objects.all()
    
    contexto = {"trabajadores": empleados_actualizados}
    
    return render(request, "AppWeb/buscar_empleado.html", contexto)

# VIEWS BASADAS EN CLASES


# Área
class ListaDepartamento(LoginRequiredMixin, ListView):
    
    model = Departamento
    
    
class DetalleDepartamento(LoginRequiredMixin, DetailView):
    
    model = Departamento
    
class CrearDepartamento(LoginRequiredMixin, CreateView):
    
    model = Departamento
    success_url = "/Web/Departamento/list"
    fields = ["nombre", "descripcion"]
    
    
class ActualizarDepartamento(LoginRequiredMixin, UpdateView):
     
    model = Departamento
    success_url = "/Web/Departamento/list"
    fields = ["nombre", "descripcion"]
    
class BorrarDepartamento(LoginRequiredMixin, DeleteView):
    
    model = Departamento
    success_url = "/Web/Departamento/list"
    
    
    
    
#Eventos
class ListaEventos(LoginRequiredMixin, ListView):
    
    model = Eventos
    
    
class DetalleEventos(LoginRequiredMixin, DetailView):
    
    model = Eventos
    
class CrearEventos(LoginRequiredMixin, CreateView):
    
    model = Eventos
    success_url = "/Web/Eventos/list"
    fields = ["nombre", "descripcion", "fecha"]
    
    
class ActualizarEventos(LoginRequiredMixin, UpdateView):
     
    model = Eventos
    success_url = "/Web/Eventos/list"
    fields = ["nombre", "descripcion", "fecha"]
    
class BorrarEventos(LoginRequiredMixin, DeleteView):
    
    model = Eventos
    success_url = "/Web/Eventos/list"
    
    
#LOGIN Y REGISTRO


def inicioSesion(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            
            contra=form.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contra)
            
            if user:
                
                login(request, user)
                
                return render(request, "AppWeb/inicio.html", {"mensaje":f"Bienvenido {user}"})
            
        else:
            
            return render(request, "AppWeb/inicio.html", {"mensaje":"Datos incorrectos."})
        
    else: 
        
        form = AuthenticationForm()
        
    
    return render(request, "AppWeb/login.html", {"formu":form})


def registro(request):
    
    if request.method =="POST":
        
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"AppWeb/inicio.html", {"mensaje":"Usuario Creado."})
        
    else: 
        
        form = UsuarioRegistro()
        
    
    return render(request, "AppWeb/registro.html", {"formu":form})

@login_required
def editar_usuario(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = FormularioEditar(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.firs_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            usuario.set_password(info["password1"])
            
            usuario.save()
            
            return render(request, "AppWeb/inicio.html")
        
    else:
        
        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            
        })
        
    return render(request, "AppWeb/editarperfil.html", {"form":form, "usuario":usuario})


def logout_view(request):
    
    logout(request)
    return render(request, "AppWeb/inicio.html", {"mensaje":"Se ha cerrado sesión"})
    

@login_required
def agregarAvatar(request):
    
    if request.method == "POST":
        
        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            
            avatar.save()
            return render(request, "AppWeb/inicio.html", {"mensaje":"Se agregó el avatar con éxito."})
        
    else:
        form = AvatarFormulario
        
    return render(request, "AppWeb/agregarAvatar.html", {"formulario":form})




    
    