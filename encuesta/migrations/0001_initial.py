# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_text', models.CharField(max_length=200)),
                ('pub_fecha', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_text', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuesta.pregunta')),
            ],
        ),
    ]