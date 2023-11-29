import pika
import json

def callback(ch, method, properties, body):
    mensagem = json.loads(body.decode('utf-8'))
    produto_id = mensagem.get('produtoId')
    quantidade_atual = mensagem.get('quantidade')

    print(f"Recebido: Produto ID {produto_id}, Quantidade Atual {quantidade_atual}")

    enviar_mensagem_outra_fila(produto_id, quantidade_atual + 100)

def enviar_mensagem_outra_fila(produto_id, nova_quantidade):
    connection_params = pika.ConnectionParameters(
        host='localhost', 
        port=5672,         
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='estoque_queue') 

    mensagem = {'produtoId': produto_id, 'quantidade': nova_quantidade}
    mensagem_json = json.dumps(mensagem)

    channel.basic_publish(
        exchange='',
        routing_key='estoque_queue',
        body=mensagem_json
    )

    connection.close()

def start_processing():
    connection_params = pika.ConnectionParameters(
        host='localhost', 
        port=5672,        
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='pedido_queue')

    channel.basic_consume(
        queue='pedido_queue',
        on_message_callback=callback,
        auto_ack=True
    )

    print("Processador aguardando mensagens. Para sair, pressione CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    start_processing()