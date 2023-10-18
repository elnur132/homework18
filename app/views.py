from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.http import HttpResponse, HttpResponseRedirect

from .models import Name

# Create your views here.
class CreateName(CreateView):
    model = Name
    fields = ['name']
    template_name = 'create_name.html'
    success_url = reverse_lazy('list')
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        obj = Name.objects.create(name=data['name'])
        return HttpResponseRedirect('list')

class ListName(ListView):
    model = Name
    template_name = 'name.html'
    context_object_name = 'names'