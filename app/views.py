import csv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Dht


def home(request):
    return render(request, 'pages/index.html')


def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'pages/tables.html', s)


def dht13(request):
    tab1 = Dht.objects.all()
    s1 = {'tab1': tab1[len(tab1)-72:len(tab1)]}
    return render(request, 'pages/Last24.html', s1)


def dht12(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'pages/graphe.html', s)


def exp_csv(request):
    obj = Dht.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHTtable.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'DT'])

    studs = obj.values_list('id', 'temp', 'dt')
    for std in studs:
        writer.writerow(std)
    return response


def exp_csv1(request):
    obj = Dht.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=Dernier24h.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'DT'])

    studs = obj.values_list('id', 'temp', 'dt')[len(obj)-72:len(obj)]
    for std in studs:
        writer.writerow(std)
    return response