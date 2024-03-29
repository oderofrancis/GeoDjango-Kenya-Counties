from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('county/',county,name='county'),
    path('county/view',countydata,name='countys'),
    path('const/',const,name='const'),
    path('county_table/',county_table,name='county_table'),
    path('const_table/',const_table,name='const_table'),
    path('county_data/',county_data,name='county_data'),
    path('const_data/',const_data,name='const_data'),
    path('ward_data/',ward_data,name='ward_data'),
    path('incidence/',incidence_data,name='incidence'),

    # form
    path('incidence_form/',incidence_form,name='incidence_form'),
]
