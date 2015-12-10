# coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=45,unique=True)

    class Meta:
        #managed = False
        db_table = 'categoria'
        verbose_name = "Categorias"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.nombre

class Reportaje(models.Model):
	estado = (
    ('pendiente', 'pendiente'),
    ('terminado', 'terminado'),)
	titulo = models.CharField(max_length=150)
	lead = models.TextField(max_length=300)
	nota = models.TextField(max_length=300, blank=True)
	tags = models.CharField(max_length=100, blank=True)
	fecha = models.DateField(blank=True)
	estado = models.CharField(max_length=50,choices=estado)
	reportero = models.ForeignKey(User,default=None,verbose_name = "Reportero")

	class Meta:
		db_table = 'Reportaje'
		verbose_name = "Reportaje"
		verbose_name_plural = "Reportajes"

	def __unicode__(self):
		return self.titulo

class Imagen(models.Model):
	imagen = models.ImageField(upload_to="imagen_reportaje/",blank=False,null=False,verbose_name = "Imagen")
	titulo = models.CharField(max_length=255, verbose_name='Titulo',blank=True,null=True)
	reportaje = models.ForeignKey('Reportaje', db_column='reportaje',verbose_name = "Reportaje")
    
	class Meta:
        #managed = False
		db_table = 'imagen'
		verbose_name = "Imagen"
		verbose_name_plural = "Imagenes"
	def __unicode__(self):
		return "[%s] %s"%(self.titulo,self.reportaje)

class Audio(models.Model):
	audio = models.FileField(upload_to="audio_reportaje/",blank=False,null=False,verbose_name = "Audio")
	titulo = models.CharField(max_length=255, verbose_name='Titulo',blank=True,null=True)
	reportaje = models.ForeignKey('Reportaje', db_column='reportaje',verbose_name = "Reportaje")
    
	class Meta:
        #managed = False
		db_table = 'audio'
		verbose_name = "Audio"
		verbose_name_plural = "Audios"
	def __unicode__(self):
		return "[%s] %s"%(self.titulo,self.reportaje)

class Video(models.Model):
	video = models.FileField(upload_to="video_reportaje/",blank=False,null=False,verbose_name = "Video")
	titulo = models.CharField(max_length=255, verbose_name='Titulo',blank=True,null=True)
	reportaje = models.ForeignKey('Reportaje', db_column='reportaje',verbose_name = "Reportaje")
    
	class Meta:
        #managed = False
		db_table = 'video'
		verbose_name = "Video"
		verbose_name_plural = "Videos"
	def __unicode__(self):
		return "[%s] %s"%(self.titulo,self.reportaje)