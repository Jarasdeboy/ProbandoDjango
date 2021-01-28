from django.http import HttpResponse
from django.shortcuts import render

def moneda(request):
    num = 0
    context = {'num' : num}
    return render(request, 'polls/moneda.html', context)

def index(request):
    return render(request, 'polls/index.html')

def saludo(request, nombre):
    context  = {'name' : nombre}
    return render(request, 'polls/saludo.html', context)