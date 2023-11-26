from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.contrib import messages
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
        messages.success(request, 'Produto criado com sucesso')
        return redirect('produtos')
    
def editarProduto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "GET":
        template = loader.get_template('editarProduto.html')
        context = {
            'produto': produto,
        }
        return HttpResponse(template.render(context, request))
    else:
        nome = request.POST.get('nome')
        data_de_ultima_compra = request.POST.get('data_de_ultima_compra')
        quantidade = request.POST.get('quantidade')
        produto.nome = nome
        produto.data_de_ultima_compra = data_de_ultima_compra
        produto.quantidade = quantidade
        produto.save()
        messages.success(request, 'Produto atualizado com sucesso')
        return redirect('produtos')

def deletarProduto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso')
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