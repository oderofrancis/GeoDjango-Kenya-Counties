# Generated by Django 3.2 on 2023-03-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0004_alter_incidence_constituency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidence',
            options={'verbose_name_plural': 'Incidences'},
        ),
        migrations.AlterField(
            model_name='incidence',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
