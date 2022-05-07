from distutils.command import upload
from turtle import update
from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    subtitulo = models.CharField(max_length=200,verbose_name="SubTitulo")
    descripcion = models.CharField(max_length=1500,verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de Edicion")
    
    def __str__(self):
        return self.titulo
    

class Contact(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nombre")
    email = models.EmailField()  
    subject = models.CharField(max_length=150,verbose_name="Asunto")
    message = models.CharField(max_length=400,verbose_name="Mensaje")
    
    def __str__(self):
        return self.name