from django.db import models

# Create your models here.
# agregamos el verbose name para camibar los nombres de los campos que se encuentrar en el administrador
class Project (models.Model):
  title = models.CharField(max_length=200, verbose_name = "Título")
  descripcion = models.TextField(verbose_name = "Descripción")
  image = models.ImageField(verbose_name = "Imagen", upload_to="projects")
  link = models.URLField(null=True, blank= True, verbose_name = "Direccion web")
  create_at = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
  update_at = models.DateField(auto_now=True, verbose_name = "Fecha de edición")

  # agregamos esto para cambiar el panel del administrador
  class Meta:
    verbose_name = "proyecto"
    verbose_name_plural = "Proyectos"
    ordering = ["-create_at"]

  def __str__(self):
    return self.title