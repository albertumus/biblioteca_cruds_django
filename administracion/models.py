from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    biografia = models.TextField(max_length=500, blank=True)
    localizacion = models.CharField(max_length=30, blank=True)
    edad = models.IntegerField(null=True)

class ActivoCM(models.Manager):
    def activos(self):
        return self.model.objects.filter( activo = True )

class ModeloActivo(models.Model):
    activo = models.BooleanField( default=True, editable=False)
    fecha_alta = models.DateTimeField( auto_now_add=True )
    fecha_modificacion = models.DateTimeField( auto_now=True )
    creado_por = models.ForeignKey( get_user_model(), related_name='%(class)s_creado_por', on_delete=models.PROTECT, null=True)
    objects = ActivoCM()

class Registro(models.Model):
    content_type = models.ForeignKey( ContentType, on_delete=models.PROTECT )
    object_id = models.CharField(max_length=300)
    objeto_modificado = GenericForeignKey( "content_type", "object_id" )
    fecha = models.DateTimeField( auto_now_add=True )
    registro_usuario = models.ForeignKey( settings.AUTH_USER_MODEL, related_name="registro_usuario", on_delete=models.PROTECT, null=True)
    tipo_acceso = models.IntegerField()

    class Meta:
        ordering = ( 'fecha', )
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

