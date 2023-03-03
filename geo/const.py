import os
from django.contrib.gis.utils import LayerMapping
from .models import Constituency

# Auto-generated `LayerMapping` dictionary for County model
constituency_mapping = {
    'county_code': 'county_code',
    'county': 'county',
    'const_code': 'const_code',
    'const': 'const',
    'geom': 'MULTIPOLYGON',
}

constituency_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data', 'constituencys.geojson'))

def run(verbose=True):
    lm = LayerMapping(Constituency, constituency_shp,constituency_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
