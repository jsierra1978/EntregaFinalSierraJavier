from email.mime import image
from venv import create
from django.contrib import admin
from core.models import Project, Contact

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=("titulo", "subtitulo", "image", "created", "updated")

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact)
