from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.serializers import serialize
import geopandas as gpd

# Create your views here.

def home(request):
    return render(request,'home.html')

def county(request):
    data = serialize('geojson',County.objects.all())
    data = gpd.read_file(data)

    # ascending order
    data = data.sort_values(by=['code'], ascending=True)
    countyNames = data['name'].tolist()
    countyValues = data['code'].tolist()

    context = {
        'countyNames':countyNames,
        'countyValues':countyValues,
    }

    return render(request,'county.html',context)

def const(request):
    return render(request,'const.html')

def county_table(request):
    return render(request,'county_table.html')

def const_table(request):
    return render(request,'const_table.html')


def county_data(request):
    data = serialize('geojson',County.objects.all())
    return HttpResponse(data,content_type='application/json')

def const_data(request):
    data = serialize('geojson',Constituency.objects.all())
    return HttpResponse(data,content_type='application/json')
