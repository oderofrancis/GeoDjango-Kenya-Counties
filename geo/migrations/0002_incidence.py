# Generated by Django 3.2 on 2023-03-07 18:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=250, null=True)),
                ('date_reported', models.DateTimeField(auto_now_add=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.constituency')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.county')),
            ],
            options={
                'verbose_name_plural': 'Incidence',
            },
        ),
    ]