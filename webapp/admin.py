from django.contrib import admin
from models import *
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display   = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)

class ReportajeAdmin(admin.ModelAdmin):
    list_display   = ('titulo',)
    ordering = ('titulo',)
    search_fields = ('titulo',)

class ImagenAdmin(admin.ModelAdmin):
    list_display   = ('id','titulo','reportaje')
    ordering = ('titulo',)
    search_fields = ('titulo',)

class AudioAdmin(admin.ModelAdmin):
    list_display   = ('id','titulo','reportaje')
    ordering = ('titulo',)
    search_fields = ('titulo',)

class VideoAdmin(admin.ModelAdmin):
    list_display   = ('id','titulo','reportaje')
    ordering = ('titulo',)
    search_fields = ('titulo',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Reportaje,ReportajeAdmin)
admin.site.register(Imagen,ImagenAdmin)
admin.site.register(Audio,AudioAdmin)
admin.site.register(Video,VideoAdmin)