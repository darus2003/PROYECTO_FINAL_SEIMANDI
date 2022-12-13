from django.db import models
from .choices import sexos
from datetime import date, time, datetime

# Create your models here.
class Provincia(models.Model):
    nombre= models.CharField(max_length=100, verbose_name= 'Provincia')

    def provincia(self):
       return "{}".format(self.nombre)

    class Meta:
       verbose_name= 'Provincia'
       verbose_name_plural= 'Provincias'
       db_table= 'provincia'
       ordering= ['nombre']


class Ciudad(models.Model):
    nombre_ciudad=models.CharField (max_length=100, verbose_name= 'Nombre') 
    codigo_postal=models.CharField (max_length=7, verbose_name= 'Codigo Postal')  
    provincia= models.ForeignKey(Provincia, null=True, on_delete=models.RESTRICT )

    def Ciudad(self):
       return "{}".format(self.nombre_ciudad)

    class Meta:
       verbose_name= 'Ciudad'
       verbose_name_plural= 'Ciudades'
       db_table= 'ciudad'
       ordering= ['nombre_ciudad']

class Familia(models.Model):
    nombre=models.CharField (max_length=100, verbose_name= 'Nombre')
    apellido_paterno=models.CharField (max_length=100, verbose_name= 'Apellido Paterno')
    apellido_materno=models.CharField (max_length=100, verbose_name= 'Apellido Materno')
    direccion= models.CharField (max_length=100, verbose_name= 'Dirección')
    ciudad=models.ForeignKey(Ciudad, null=True, on_delete=models.RESTRICT )
    fecha_nacimiento=models.DateField(verbose_name= 'Fecha de Nacimiento' )
    sexo=models.CharField(max_length=1, choices=sexos, default='F' )

    def nombre_completo(self):
        return '{} {}, {}'.format(self.apellido_paterno, self.apellido_materno, self.nombre)

    def __str__(self):
        return self.nombre_completo

    class Meta:
       verbose_name= 'Familia'
       verbose_name_plural= 'Familiares'
       db_table= 'familia'
       ordering= ['apellido_paterno', 'apellido_materno', 'nombre']












