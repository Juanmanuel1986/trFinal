from django.db import models

# Create your models here.
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    equipo = models.CharField(max_length=100, verbose_name='Equipo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    jira = models.CharField(max_length=30, verbose_name='Jira')
    devops = models.CharField(max_length=50, verbose_name='Devops')
    refDev = models.CharField(max_length=100, verbose_name='Referente Dev')
    refQA = models.CharField(max_length=100, verbose_name='Referente QA')
    nvlCode = models.IntegerField(max_length=30, verbose_name='Nivel Calidad Codigo') 
    nvlAuto = models.IntegerField(max_length=30, verbose_name='Nivel Regression QA') 
    comentario = models.CharField(max_length=500, verbose_name='Comentario')

    def __str__(self):
        fila = "Equipo: " + self.equipo
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()






                  