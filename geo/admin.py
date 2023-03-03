from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class CountyAdmin(LeafletGeoAdmin):
    list_display = ('name','code')

admin.site.register(County,CountyAdmin)

class ConstituencyAdmin(LeafletGeoAdmin):
    list_display = ('const','county','const_code')

admin.site.register(Constituency,ConstituencyAdmin)