from django.db import models

# Create your models here.
class paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    docuemnto = models.IntegerField()
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=2)
    pais = models.CharField(max_length=100)
    
class sesion(models.Model):
    paciente_id   = models.IntegerField()
    fecha_sesion  = models.DateField
    valor_sesion  = models.IntegerField()
    estado_sesion = models.CharField(max_length=40)
