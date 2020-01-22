from django.db import models

from django.db.models.signals import post_delete, post_save
from administracion.models import ModeloActivo, Registro

class Tematica(ModeloActivo):
    nombre = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Temática'
        verbose_name_plural = 'Temáticas'

class Autor(ModeloActivo):
    nombre = models.CharField(max_length=300, blank=False, null=False)
    nacimiento =  models.DateField(auto_now_add=False)
    ciudad = models.CharField(max_length=300, blank=False, null=False)
    temas = models.ManyToManyField(Tematica)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Editorial(ModeloActivo):
    nombre = models.CharField(max_length=300, blank=False, null=False)
    fecha_creacion = models.DateField(auto_now_add=False)
    ciudad = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

class Libro(ModeloActivo):
    titulo = models.CharField(max_length=300, blank=False, null=False)
    autor_libro = models.ForeignKey(Autor, on_delete=models.PROTECT)
    editorial_libro = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    documento = models.FileField(upload_to='documents/', null=True, blank=True)
    

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

clases = [Libro, Autor, Editorial, Tematica]

def crear_actualizar_registro( sender, instance, created, **kwargs ):
    if created:
        r = Registro( objeto_modificado=instance, registro_usuario=instance.creado_por , tipo_acceso=0)
    else:
        r = r = Registro( objeto_modificado=instance, registro_usuario=instance.creado_por ,tipo_acceso=1)
    
    r.save()

def eliminar_registro( sender, instance, **kwargs ):
    r = Registro( objeto_modificado=instance, registro_usuario=instance.creado_por, tipo_acceso =2)
    r.save()

for clase in clases:
    post_save.connect( crear_actualizar_registro, sender=clase, dispatch_uid="att_post_save_"+clase.__name__) 
    post_delete.connect( eliminar_registro, sender=clase, dispatch_uid="att_post_delete_"+clase.__name__) 

