from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class ActivoCM(models.Manager):
    def activos(self):
        return self.model.objects.filter( activo = True )

class ModeloActivo(models.Model):
    activo = models.BooleanField( default=True, editable=False)
    fecha_alta = models.DateTimeField( auto_now_add=True )
    fecha_modificacion = models.DateTimeField( auto_now=True )
    objects = ActivoCM()

class Registro(models.Model):
    content_type = models.ForeignKey( ContentType, on_delete=models.PROTECT )
    object_id = models.CharField(max_length=300)
    objeto_modificado = GenericForeignKey( "content_type", "object_id" )
    fecha = models.DateTimeField( auto_now_add=True )
    tipo_acceso = models.IntegerField()

    class Meta:
        ordering = ( 'fecha', )
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

