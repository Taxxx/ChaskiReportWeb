# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20151210_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportaje',
            name='categoria',
            field=models.ForeignKey(default=None, verbose_name='Categoria', to='webapp.Categoria'),
            preserve_default=True,
        ),
    ]
