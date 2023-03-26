import os
from django.contrib.gis.utils import LayerMapping
from .models import *

# Auto-generated `LayerMapping` dictionary for Ward model
ward_mapping = {
    'county': 'county',
    'const': 'const',
    'ward': 'ward',
    'ward_code': 'ward_code',
    'geom': 'MULTIPOLYGON',
}

ward_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data', 'ward.geojson'))

def run(verbose=True):
    lm = LayerMapping(Ward, ward_shp,ward_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)