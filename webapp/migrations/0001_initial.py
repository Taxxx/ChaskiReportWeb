# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audio', models.FileField(upload_to='audio_reportaje/', verbose_name='Audio')),
                ('titulo', models.CharField(max_length=255, null=True, verbose_name='Titulo', blank=True)),
            ],
            options={
                'db_table': 'audio',
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'categoria',
                'verbose_name': 'Categorias',
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to='imagen_reportaje/', verbose_name='Imagen')),
                ('titulo', models.CharField(max_length=255, null=True, verbose_name='Titulo', blank=True)),
            ],
            options={
                'db_table': 'imagen',
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reportaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=150)),
                ('lead', models.TextField(max_length=300)),
                ('nota', models.TextField(max_length=300, blank=True)),
                ('tags', models.CharField(max_length=100, blank=True)),
                ('fecha', models.DateField(blank=True)),
                ('estado', models.CharField(max_length=50, choices=[('pendiente', 'pendiente'), ('terminado', 'terminado')])),
                ('reportero', models.ForeignKey(default=None, verbose_name='Reportero', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Reportaje',
                'verbose_name': 'Reportaje',
                'verbose_name_plural': 'Reportajes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audio', models.FileField(upload_to='video_reportaje/', verbose_name='Video')),
                ('titulo', models.CharField(max_length=255, null=True, verbose_name='Titulo', blank=True)),
                ('reportaje', models.ForeignKey(db_column='reportaje', verbose_name='Reportaje', to='webapp.Reportaje')),
            ],
            options={
                'db_table': 'video',
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagen',
            name='reportaje',
            field=models.ForeignKey(db_column='reportaje', verbose_name='Reportaje', to='webapp.Reportaje'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='audio',
            name='reportaje',
            field=models.ForeignKey(db_column='reportaje', verbose_name='Reportaje', to='webapp.Reportaje'),
            preserve_default=True,
        ),
    ]
