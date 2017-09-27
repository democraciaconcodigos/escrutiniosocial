# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields
import elecciones.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Circuito electoral',
                'verbose_name_plural': 'Circuitos electorales',
                'ordering': ('numero',),
            },
        ),
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Elección',
                'verbose_name_plural': 'Elecciones',
            },
        ),
        migrations.CreateModel(
            name='LugarVotacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('barrio', models.CharField(blank=True, max_length=100)),
                ('ciudad', models.CharField(blank=True, max_length=100)),
                ('calidad', models.CharField(blank=True, editable=False, help_text='calidad de la geolocalizacion', max_length=20)),
                ('electores', models.PositiveIntegerField(blank=True, null=True)),
                ('geom', djgeojson.fields.PointField(null=True)),
                ('latitud', models.FloatField(editable=False, null=True)),
                ('longitud', models.FloatField(editable=False, null=True)),
                ('circuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elecciones.Circuito')),
            ],
            options={
                'verbose_name': 'Lugar de votación',
                'verbose_name_plural': 'Lugares de votación',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('es_testigo', models.BooleanField(default=False)),
                ('url_datos_oficiales', models.URLField(blank=True, help_text='url al telegrama')),
                ('url_pdf_datos_oficiales', models.URLField(blank=True, help_text='url al pdf del telegrama')),
                ('foto_acta', models.ImageField(blank=True, null=True, upload_to=elecciones.models.path_foto_acta)),
                ('electores', models.PositiveIntegerField(blank=True, null=True)),
                ('eleccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elecciones.Eleccion')),
                ('lugar_votacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mesas', to='elecciones.LugarVotacion', verbose_name='Lugar de votacion')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_corto', models.CharField(default='', max_length=10)),
                ('orden', models.PositiveIntegerField(blank=True, help_text='Orden en la boleta', null=True)),
                ('obligatorio', models.BooleanField(default=False)),
                ('es_contable', models.BooleanField(default=True)),
                ('codigo_dne', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Opción',
                'verbose_name_plural': 'Opciones',
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.PositiveIntegerField(help_text='Orden opcion')),
                ('numero', models.PositiveIntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_corto', models.CharField(blank=True, max_length=10)),
                ('color', models.CharField(blank=True, max_length=30)),
                ('obligatorio', models.BooleanField(default=False)),
                ('es_contable', models.BooleanField(default=True)),
                ('codigo_dne', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sección electoral',
                'verbose_name_plural': 'Secciones electorales',
            },
        ),
        migrations.AddField(
            model_name='opcion',
            name='partido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elecciones.Partido'),
        ),
        migrations.AddField(
            model_name='eleccion',
            name='opciones',
            field=models.ManyToManyField(to='elecciones.Opcion'),
        ),
        migrations.AddField(
            model_name='circuito',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elecciones.Seccion'),
        ),
    ]