from django.urls import path
from AppWeb.views import *
from .views import logout_view
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('acercaDeMi/', acercaDeMi, name='acercaDeMi'),
    
    path('ConfirmacionDeInformacionGuardada/', confirmacion_guardar),
    
    path('consulta_nueva/', consultas, name= 'consulta_nueva'),
    
    path('buscar_empleado/', buscar_empleado, name='buscar_empleado'),
    
    path('resultados/', resultado_empleado),
    
    #LOGIN
    path('login/', inicioSesion, name="login"),
    path('register/', registro, name="Registro"),
    path('logout/', logout_view, name='logout'),
    path('editar/', editar_usuario, name='editar'),
    path("verConsultas", leerConsultas, name='verConsultas'),
    #Avatar
    path('agregarAvatar', agregarAvatar, name="avatar"),
    

        
    
    #CRUD de empleados
    
    path('empleados/', LeerEmpleados, name= 'Empleados'),
    path('empleadoNuevo/', empleado_nuevo, name='empleado_nuevo'),
    path('EliminarEmpleado<empleadoNombre>', eliminarEmpleado, name= 'EliminarEmpleado'),   
    
    
    #CRUD USANDO CLASES
    
    #Área
    path('Departamento/list/', ListaDepartamento.as_view(), name= 'LeerDepartamento'),
    path('Departamento/<int:pk>/', DetalleDepartamento.as_view(), name= 'DetalleDepartamento'),
    path('Departamento/crear/', CrearDepartamento.as_view(), name= 'CrearDepartamento'),
    path('Departamento/editar/<int:pk>', ActualizarDepartamento.as_view(), name= 'ActualizarDepartamento'),   
    path('Departamento/borrar/<int:pk>', BorrarDepartamento.as_view(), name= 'BorrarDepartamento'),
    
    #Eventos
    path('Eventos/list/', ListaEventos.as_view(), name= 'LeerEventos'),
    path('Eventos/<int:pk>/', DetalleEventos.as_view(), name= 'DetalleEventos'),
    path('Eventos/crear/', CrearEventos.as_view(), name= 'CrearEventos'),
    path('Eventos/editar/<int:pk>', ActualizarEventos.as_view(), name= 'ActualizarEventos'),   
    path('Eventos/borrar/<int:pk>', BorrarEventos.as_view(), name= 'BorrarEventos'),
    
]