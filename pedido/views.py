from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from .models import Pedido

@login_required
def pedir(request):
    return HttpResponse('Pedir')

@login_required
def pedidos(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

    pedidos = Pedido.objects.filter(usuario=request.user)
    context = {'pedidos': pedidos}

    return render(request, 'pedidos.html', context)