from django.db import models
from django.db.models import Manager as GeoManager
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

class Incidence(models.Model):
    title = models.CharField(max_length=200)
    Constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    description =models.TextField(max_length=250, null=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Incidence'