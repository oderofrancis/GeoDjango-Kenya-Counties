# Generated by Django 3.2 on 2023-03-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0005_auto_20230308_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidence',
            name='constituency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.constituency'),
        ),
    ]
