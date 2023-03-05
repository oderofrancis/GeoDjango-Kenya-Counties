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

    showmap = 'True'

    context = {
        'countyNames':countyNames,
        'countyValues':countyValues,
        'showmap':showmap,
    }

    return render(request,'county.html',context)

def countydata(request):

    countynames = request.POST.get('countynames')

    data = serialize('geojson',County.objects.all())
    data = gpd.read_file(data)
    data = data.sort_values(by=['code'], ascending=True)
    countyNames = data['name'].tolist()
    countyValues = data['code'].tolist()

    # constituency

    datas = serialize('geojson',Constituency.objects.all())
    datas = gpd.read_file(datas)

    datas = datas[datas['county']==countynames]
    datas = datas.sort_values(by=['const_code'], ascending=True)
    constNames = datas['const'].str.replace(' ','-').tolist()
    constValues = datas['const_code'].tolist()

    # map data

    showmap = 'False'

    context = {
        'countynames':countynames,
        'countyNames':countyNames,
        'countyValues':countyValues,
        'showmap':showmap,

        'constNames':constNames,
        'constValues':constValues,
    }

    return render(request,'county.html',context)


def const(request):
    data = serialize('geojson',Constituency.objects.all())
    data = gpd.read_file(data)

    # ascending order
    data = data.sort_values(by=['const_code'], ascending=True)
    countyNames = data['const'].tolist()
    countyValues = data['const_code'].tolist()

    context = {
        'countyNames':countyNames,
        'countyValues':countyValues,
    }
    return render(request,'const.html',context)

def county_table(request):
    data = County.objects.all()

    context = {
        'data':data
    }
    return render(request,'county_table.html',context)

def const_table(request):
    data = Constituency.objects.all()

    context = {
        'data':data
    }
    return render(request,'const_table.html',context)


def county_data(request):
    data = serialize('geojson',County.objects.all())
    return HttpResponse(data,content_type='application/json')

def const_data(request):
    data = serialize('geojson',Constituency.objects.all())
    return HttpResponse(data,content_type='application/json')
