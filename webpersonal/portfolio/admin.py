from django.contrib import admin
from .models import Project
# Register your models here.

#hacemos una una clase para mostrar campos escondidos como solo lectura de los 
class ProjectAdmin(admin.ModelAdmin):
  readonly_fields = ('create_at','update_at')


admin.site.register(Project, ProjectAdmin)
