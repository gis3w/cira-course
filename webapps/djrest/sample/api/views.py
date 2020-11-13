#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:32:11 2020

@author: walter
"""

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
#from rest_framework import permissions
from sample.models import Sample, SampleGeo
from .serializers import \
    SampleSerializer, \
    SimpleSampleSerializer, \
    SampleGeoSerializer


# DRF docs:
# https://www.django-rest-framework.org/api-guide/views/
# https://www.django-rest-framework.org/api-guide/generic-views/
# https://www.django-rest-framework.org/api-guide/viewsets/



class SampleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows samples to be viewed or edited.
    """
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    #permission_classes = [permissions.IsAuthenticated]
    

class SampleListViewSet(ListAPIView):
    """
    API endpoint that allows samples to be viewed only.
    """
    queryset = Sample.objects.all()
    serializer_class = SimpleSampleSerializer
    

class SampleGeoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows samples GEO to be viewed or edited.
    """
    queryset = SampleGeo.objects.all()
    serializer_class = SampleGeoSerializer
    #permission_classes = [permissions.IsAuthenticated]