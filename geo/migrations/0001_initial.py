# Generated by Django 3.2 on 2023-03-03 10:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county_code', models.IntegerField()),
                ('county', models.CharField(max_length=100)),
                ('const_code', models.IntegerField()),
                ('const', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Constituency',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'County',
            },
        ),
    ]
