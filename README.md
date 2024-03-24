# WEB

## El fin de este proyecto es hacer una pequeña web para un área de RR.HH de una empresa donde pueda manejarse los eventos importantes, empledos nuevos, consultas de los empleados y se puedan ver las distintas áreas de la empresa según fueran creadas. 

# Desde la terminal de VSC:


1. Realizar las migraciones correspondientes para la base de datos con :

 `python manage.py makemigratios`
 
 Seguido de: 
 
 `python manage.py migrate`

2. Para utilizar el administrador se debe crear un superuser con el siguiente comando:

`python manage.py createsuperuser`

Yo ya he creado un `superuser` con las siguientes credenciales:

* username: gonzalo

* contraseña: milanesa



3. Para hacer funcionar el servidor colocar: 

`python manage.py runserver`


# Pruebas:

Una vez el servidor esté funcionando estan estas urls disponibles para utilizar según las funciones de la página web. Según accione uno de los botones podrá guardar la información que se solicita o buscar y obtener resultados dentro de la misma plataforma.

### URLS:


`1. admin/`

`2. Web/ [name='inicio']`

`3. Web/ acercaDeMi/ [name='acercaDeMi']`

`4. Web/ ConfirmacionDeInformacionGuardada/`

`5. Web/ consulta_nueva/ [name='consulta_nueva']`

`6. Web/ buscar_empleado/ [name='buscar_empleado']`

`7. Web/ resultados/`

`8. Web/ login/ [name='login']`

`9. Web/ register/ [name='Registro']`

`10. Web/ logout/ [name='logout']`

`11. Web/ editar/ [name='editar']`

`12. Web/ verConsultas [name='verConsultas']`

`13. Web/ agregarAvatar [name='avatar']`

`14. Web/ empleados/ [name='Empleados']`

`15. Web/ empleadoNuevo/ [name='empleado_nuevo']`

`16. Web/ EliminarEmpleado<empleadoNombre> [name='EliminarEmpleado']`

`17. Web/ Departamento/list/ [name='LeerDepartamento']`

`18. Web/ Departamento/<int:pk>/ [name='DetalleDepartamento']`

`19. Web/ Departamento/crear/ [name='CrearDepartamento']`

`20. Web/ Departamento/editar/<int:pk> [name='ActualizarDepartamento']`

`21. Web/ Departamento/borrar/<int:pk> [name='BorrarDepartamento']`

`22. Web/ Eventos/list/ [name='LeerEventos']`

`23. Web/ Eventos/<int:pk>/ [name='DetalleEventos']`

`24. Web/ Eventos/crear/ [name='CrearEventos']`

`25. Web/ Eventos/editar/<int:pk> [name='ActualizarEventos']`

`26. Web/ Eventos/borrar/<int:pk> [name='BorrarEventos']`



# Modelos

Esta página consta de 5 modelos.

`Empleado`

`Consultas`

`Departamento`

`Eventos`

`Avatar`


# Formularios


La web consta de 7 formularios que ayudan a su funcionamiento.

`FormularioEmpleado`

`FormularioConsultas`

`FormularioDepartamento`

`FormularioEventos`

`UsuarioRegistro`

`FormularioEditar`

`AvatarFormulario`
    



# Contacto:

gonzaloconti@hotmail.com


