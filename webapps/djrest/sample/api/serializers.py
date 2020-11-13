#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:32:30 2020

@author: walter
"""

# DRF docs:
# https://www.django-rest-framework.org/api-guide/serializers/

# DRF-GIS docs:
# https://github.com/openwisp/django-rest-framework-gis

from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers
from sample.models import Sample, SampleGeo




class SampleSerializer(serializers.HyperlinkedModelSerializer):
    "Very simple serilizer"
    
    class Meta:
        model = Sample
        fields = '__all__'
        
class SimpleSampleSerializer(serializers.ModelSerializer):
    "Very simple serilizer"
    
    class Meta:
        model = Sample
        fields = '__all__'

class SampleGeoSerializer(geo_serializers.GeoFeatureModelSerializer):
    class Meta:
        model = SampleGeo
        geo_field = 'geom'
        fields = '__all__'