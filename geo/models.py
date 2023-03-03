from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    geom = models.GeometryField(srid=4326)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'County'

class Constituency(models.Model):
    county_code = models.IntegerField()
    county = models.CharField(max_length=100)
    const_code = models.IntegerField()
    const = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.const
    
    class Meta:
        verbose_name_plural = 'Constituency'
