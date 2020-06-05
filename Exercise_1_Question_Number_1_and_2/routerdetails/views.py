from django.shortcuts import render
from django.http import HttpResponse
from .models import routerdeails
from django.views.generic import CreateView,ListView,DetailView,UpdateView



# Create your views here.
def home(request):
    return HttpResponse('<h1>Heyyy I am in </h1>')


class AddSiteDetails(CreateView):
    model = routerdeails
    fields = ['sapid','hostname','loopback','macadress','active_flag']
    # success_url = reverse('calorie_log-home')
    success_url = '/routerdetails/search'

class SerachSiteDetails(ListView):
    model = routerdeails
    # template_name = 'routerdetails/search.html'
    context_object_name = 'sites'

# class UpdateSiteDetils(UpdateView):
#     model = routerdeails
#     fields = ['sapid','hostname','loopback','macadress']


class SiteDetailView(DetailView):
    model = routerdeails

class SiteUpdateView(UpdateView):
    model = routerdeails
    fields = ['sapid','hostname','loopback','macadress','active_flag']
    success_url = '/routerdetails/search'




