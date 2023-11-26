from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Produto, Prato, PratoProduto

def produtos(request):
    produtos = Produto.objects.all()
    template = loader.get_template('produtos.html')
    context = {
        'produtos': produtos,
    }
    return HttpResponse(template.render(context, request))

def cadastrarProduto(request):
    if request.method == "GET":
        return render(request, 'cadastrarProduto.html')
    else:
        nome = request.POST.get('nome')
        data_de_ultima_compra = request.POST.get('data_de_ultima_compra')
        quantidade = request.POST.get('quantidade')
        produto = Produto.objects.create(nome=nome,data_de_ultima_compra=data_de_ultima_compra,quantidade=quantidade)
        produto.save()
        return redirect('produtos')

def pratos(request):
    pratos = Prato.objects.all()
    template = loader.get_template('pratos.html')
    context = {
        'pratos': pratos,
    }
    return HttpResponse(template.render(context, request))

def cadastrarPrato(request):
    if request.method == "GET":
        return render(request, 'cadastrarPrato.html')
    else:
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        produtos = request.POST.get('produtos')
        prato = Prato.objects.create(nome=nome,preco=preco)
        prato.save()

        for produto in produtos:
            produto = Produto.objects.get(id=produto.id)
            pratoProduto = PratoProduto.objects.create(quantidade=produto.quantidade, prato=prato, produto=produto)
            pratoProduto.save()

        return redirect('pratos')