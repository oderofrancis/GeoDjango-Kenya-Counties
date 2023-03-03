import os
from django.contrib.gis.utils import LayerMapping
from .models import County

# Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
    'name': 'name',
    'code': 'code',
    'geom': 'UNKNOWN',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data', 'countys.geojson'))

def run(verbose=True):
    lm = LayerMapping(County, county_shp, county_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)