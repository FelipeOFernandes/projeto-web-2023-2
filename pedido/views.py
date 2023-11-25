from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pedir(request):
    return HttpResponse('Pedir')

def pedidos(request):
    return HttpResponse('Pedidos')