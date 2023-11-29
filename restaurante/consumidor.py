# consumidor.py

import pika
from django.conf import settings
from estoque.models import Produto
from datetime import date
import json

def callback(ch, method, properties, body):
    mensagem = json.loads(body.decode('utf-8'))
    produtoId = mensagem.get('produtoId')
    produto = Produto.objects.get(id=produtoId)
    produto.quantidade = mensagem.get('quantidade')
    print(produto)
    produto.data_de_ultima_compra = date.today()
    produto.save()

def start_consumer():
    connection_params = pika.ConnectionParameters(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_RECIEVE_QUEUE)

    channel.basic_consume(
        queue=settings.RABBITMQ_RECIEVE_QUEUE,
        on_message_callback=callback,
        auto_ack=True
    )

    print("Consumidor aguardando mensagens. Para sair, pressione CTRL+C")
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()

    connection.close()

if __name__ == '__main__':
    start_consumer()