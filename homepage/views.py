from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Modul

def index(request):
    kelas_gratis = Modul.objects.filter(harga=0)[:5]
    kelas_terbaru = Modul.objects.order_by('-id')[:5]
    kelas_expert = Modul.objects.filter(harga__gt=0)[:4]
    context = {
        'kelas_gratis' : kelas_gratis,
        'kelas_terbaru' : kelas_terbaru,
        'kelas_expert' : kelas_expert,
    }
    template = loader.get_template('homepage/index.html')
    return HttpResponse(template.render(context, request))

def modul_detail(request, modul_id):
    data_modul = Modul.objects.get(id=modul_id)
    context = {
        'data_modul' : data_modul
    }
    template = loader.get_template('homepage/modul_detail.html')
    return HttpResponse(template.render(context, request))