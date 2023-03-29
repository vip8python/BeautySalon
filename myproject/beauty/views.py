from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views import generic


def base(request):
    return render(request, 'beauty/base.html', {'title': 'Beauty'})


def services(request):
    sevices_list = Services.objects.all()
    return render(request, 'beauty/services.html', {'services': sevices_list})


def client(request):
    pass


def specialist(request):
    specialist_list = Specialist.objects.all()
    return render(request, 'beauty/specialist.html', {'specialist': specialist_list})

def registration(request):
    pass

class SpecialistListView(generic.ListView):
    model = Specialist
    template_name = 'beauty/specialist_list.html'

class SpecialistDetailView(generic.DetailView):
    model = Specialist
    template_name = 'beauty/specialist_detail.html'


from django.db.models import Q


def search(request):
    query = request.GET.get('query')
    search_results = Specialist.objects.filter(Q(company__icontains=query) | Q(address__icontains=query))
    return render(request, 'beauty/search.html', {'specialist': search_results, 'query': query})
