import json
import pika
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.template import loader
from datetime import date
from django.conf import settings
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
        prato_id = request.POST.get('pratoId')
        prato = get_object_or_404(Prato, id=prato_id)

        for pp in prato.pratoproduto_set.all():
            produto = pp.produto
            quantidade_necessaria = pp.quantidade

            produto.quantidade -= quantidade_necessaria
            produto.save()

            if produto.quantidade < 10:
                enviar_mensagem_rabbitmq(produto.id, produto.quantidade)

        pedido = Pedido.objects.create(usuario=request.user, prato=prato, datahora=date.today())
        pedido.save()

        messages.success(request, 'Pedido criado com sucesso')
        return redirect('pedidos')

def enviar_mensagem_rabbitmq(produto_id, quantidade_atual):
    connection_params = pika.ConnectionParameters(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_SEND_QUEUE)

    mensagem = {'produtoId': produto_id, 'quantidade': quantidade_atual}
    mensagem_json = json.dumps(mensagem)

    channel.basic_publish(
        exchange='',
        routing_key=settings.RABBITMQ_SEND_QUEUE,
        body=mensagem_json
    )

    connection.close()


@login_required
def pedidos(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

    pedidos = Pedido.objects.filter(usuario_id=request.user.id)
    context = {'pedidos': pedidos}

    return render(request, 'pedidos.html', context)