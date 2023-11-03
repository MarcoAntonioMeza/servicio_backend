from django.db import models

from usuarios.models import Usuario

# Create your models here.
class Etapa(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Servicio(models.Model):
    
    folio = models.CharField(max_length=50,null=True,verbose_name='Folio')

    fecha_recibo = models.DateField(null=True,verbose_name='Fecha de recepción')
    fecha_entrega = models.DateField(null=False,verbose_name='Fecha de entrega',default=None)

    costo_aproximado = models.DecimalField(max_digits=8,decimal_places=2, null=True ,verbose_name='Costo aproximado')
    costo_final = models.DecimalField(max_digits=8,decimal_places=2,default=0, verbose_name='Costo final')


    descripcion_cliente = models.TextField(null=True,verbose_name='Descripción del cleinte')
    

    etapa = models.ForeignKey('Etapa' , on_delete=models.CASCADE)

    usuario = models.ManyToManyField(Usuario,related_name='Usuarios')

    def __str__(self):
        return f'{self.folio}'






class Equipo(models.Model):

    nombre = models.CharField(max_length=255)
    caracteristicas_posibles = models.TextField(verbose_name='Características posibles')
    caracteristicas_reales = models.TextField(null=True, blank=True,verbose_name='Características reales')

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f'Equipo {self.nombre}'
    


    
class Hallazgo(models.Model):

    nombre = models.CharField(max_length=255,verbose_name='Nombre del hallazgo')

    descripcion = models.TextField(verbose_name='Descripción del hallazgo')

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nombre}'

    
    

#Diagnostico
class Diagnostico(models.Model):

    nombre = models.CharField(max_length=200, null=True, verbose_name='Nombre diagnostico')
    foto_pieza = models.ImageField(upload_to='imagen_pieza/', null=True, blank=True)
    tiempo_instalacion = models.CharField(max_length=50, null=True, verbose_name='Tiempo de instalacion') 
    recomendacion = models.CharField(max_length=50, null=True, verbose_name='Recomendación')
    costo =  models.DecimalField(max_digits=8, decimal_places=2, null=True, verbose_name='Costo de la pieza')
    descripcion = models.TextField(verbose_name='Descripción del diagnostico')

    hallazgo = models.ForeignKey(Hallazgo, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.nombre} ${self.costo}'
    
