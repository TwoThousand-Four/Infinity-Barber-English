from django.db import models

# Create your models here.

#Clase tipo consulta
class QueryType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    
    def __str__(self):
        return self.name

#Clase Servicio
class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    description = models.CharField(max_length=150, verbose_name="Description")
    image = models.ImageField(upload_to='img/service', verbose_name="Service image", null=True)
    price =  models.IntegerField(verbose_name="Price")
    
    def __str__(self):
        return self.name
    
    #Borrar imagenes desde el admin
    def delete(self, using=None, keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
         
#Clase Contacto
class Contact (models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    query_type = models.ForeignKey(QueryType, on_delete=models.PROTECT, verbose_name="Query Type")
    message = models.TextField(max_length=1000, verbose_name="Message")
    advice = models.BooleanField(verbose_name="Advice")
    
    def __str__(self) :
        return self.name