# Generated by Django 3.2 on 2023-03-08 17:12

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0006_auto_20230308_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
