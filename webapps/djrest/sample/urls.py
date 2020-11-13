# -*- coding: utf-8 -*-

from django.urls import path, include
from .views import home_view, HomeView, HomeViewTemplate

from rest_framework import routers
from .api import views


# DRF router to build url for CRUD API operation
# docs: https://www.django-rest-framework.org/api-guide/routers/

router = routers.DefaultRouter()
router.register(r'samples', views.SampleViewSet)
router.register(r'samplegeos', views.SampleGeoViewSet)

urlpatterns = [
        #path('', home_view),
        #path('', HomeView.as_view()),
        path('', HomeViewTemplate.as_view()),
        
        # add CRUD API urls
        path('api/', include(router.urls)),
        path('api/list_samples', views.SampleListViewSet.as_view())
    ]