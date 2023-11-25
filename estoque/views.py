from django.http import HttpResponse
from django.template import loader

def produtos(request):
    return HttpResponse('Produtos')

def cadastrarProduto(request):
    return HttpResponse('Cadastrar Produto')

def pratos(request):
    return HttpResponse('Pratos')

def cadastrarPrato(request):
    return HttpResponse('Cadastrar prato')