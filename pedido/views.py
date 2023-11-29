from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.template import loader
from datetime import date
from .models import Pedido
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from estoque.models import Produto, Prato

@login_required
def pedir(request):
    if request.method == "GET":
        pratos = Prato.objects.all()
        template = loader.get_template('cadastrarPedido.html')
        context = {
            'pratos': pratos,
        }
        return HttpResponse(template.render(context, request))
    else:
        pratoId = request.POST.get('pratoId')
        prato = get_object_or_404(Prato, id=pratoId)
        pedido = Pedido.objects.create(usuario=request.user, prato=prato, datahora=date.today())
        pedido.save()

        messages.success(request, 'Pedido criado com sucesso')
        return redirect('pedidos')

@login_required
def pedidos(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

    pedidos = Pedido.objects.filter(usuario_id=request.user.id)
    context = {'pedidos': pedidos}

    return render(request, 'pedidos.html', context)