# -*- coding: utf-8 -*-

from django.urls import path
from .views import home_view, HomeView, HomeViewTemplate

urlpatterns = [
        #path('', home_view),
        #path('', HomeView.as_view()),
        path('', HomeViewTemplate.as_view()),
    ]