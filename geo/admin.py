from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class CountyAdmin(LeafletGeoAdmin):
    list_display = ('name','code')
    search_fields = ('name','code')
    filter_fields= ('name')

admin.site.register(County,CountyAdmin)

class ConstituencyAdmin(LeafletGeoAdmin):
    list_display = ('const','county','const_code')
    search_fields = ('const','county')
    filter_fields= ('const','county')

admin.site.register(Constituency,ConstituencyAdmin)

class WardAdmin(LeafletGeoAdmin):
    list_display = ('ward','const','county')
    search_fields = ('ward','const','county')
    filter_fields= ('ward','const','county')

admin.site.register(Ward,WardAdmin)

class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('title','constituency','date_reported')

admin.site.register(Incidence,IncidenceAdmin)

class mappingAdmin(LeafletGeoAdmin):
    list_display = ('name','county','constituency')

admin.site.register(mapping,mappingAdmin)