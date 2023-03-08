from .models import *
from django.contrib.gis import forms as geoforms
from django import forms



class IncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ('title', 'county', 'constituency', 'description', 'location')
        widgets = {
            'constituency': forms.Select(
                attrs={'class': 'form-control'},
            ),
        }
        widgets = {'location':  
                geoforms.OSMWidget(
                    attrs={
                    'map_width': 850, 
                    'map_height': 530,
                    'default_lat': 0.0515,
                    'default_lon': 37.7456,
                    'default_zoom':6.4,
                    'max_zoom':20,
                    'min_zoom':4,
                    }
                )
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'county') and self.instance.county:
            self.fields['constituency'].queryset = Constituency.objects.filter(
                county=self.instance.county
            )
        else:
            self.fields['constituency'].queryset = Constituency.objects.none()