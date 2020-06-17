from django.contrib import admin
from .models import Categoria,Autor,Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre',]
    list_display = ('nombre','estado','fecha_creacion',)
    resources_class = CategoriaResource

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Autor
class AutorAdmi(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','estado','fecha_creacion')

class PostAdmi( admin.ModelAdmin):
    ordering=['-titulo']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor,AutorAdmi)
admin.site.register(Post)

