#from django.db import models
from django.contrib.gis.db import models

class Sample(models.Model):
    "Very simple model NO GEO"
    
    name = models.CharField('Sample name', max_length=255)
    a_value = models.FloatField('Value A')
    b_value = models.FloatField('Value B', null=True, blank=True)
    c_value = models.BooleanField('Value boolean c', default=False)
    comment = models.TextField('Comment', null=True, blank=True)

    def __str__(self):
        return self.name


class SampleGeo(models.Model):
    "Very simple model GEO"
    
    name = models.CharField('Sample name', max_length=255)
    a_value = models.FloatField('Value A')
    b_value = models.FloatField('Value B', null=True, blank=True)
    c_value = models.BooleanField('Value boolean c', default=False)
    comment = models.TextField('Comment', null=True, blank=True)

    geom = models.PointField()

    def __str__(self):
        return self.name