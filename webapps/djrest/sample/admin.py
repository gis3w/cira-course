#from django.contrib import admin
from django.contrib.gis import admin
from .models import Sample, SampleGeo

from leaflet.admin import LeafletGeoAdminMixin
from geoadmin.admin import GeoAdminMixin


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
     list_display = ('name', 'a_value')


# Change: GeoModelAdmin -> OSMGeoAdmin

@admin.register(SampleGeo)
class SampleGeoAdmin(GeoAdminMixin, LeafletGeoAdminMixin, admin.ModelAdmin):
     list_display = ('name', 'a_value')