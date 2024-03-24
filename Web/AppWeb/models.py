from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Empleado(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    
    
    def __str__(self):

        return f"{self.nombre} --- {self.apellido} --- {self.puesto}"
    

class Consultas(models.Model):
    usuario = models.CharField(max_length=30)
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=1000)

    
    def __str__(self):

        return f"{self.titulo} --- {self.fecha}"


class Departamento(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    

    def __str__(self):

        return f"{self.nombre}"
    
class Eventos(models.Model):
    
    nombre = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField()
    
    def __str__(self):

        return f"{self.nombre}-----{self.fecha}"
    

class Avatar(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True,blank=True)
    