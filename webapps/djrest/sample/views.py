from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render

def home_view(request):
    return HttpResponse('Welcome to sample app!')

class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        
        context = {'name': 'Giorgio'}
        return render(request, template_name='home.html', context=context)
    

class HomeViewTemplate(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        return {'name': 'Amilcare'}
    