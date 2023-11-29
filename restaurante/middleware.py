from django.conf import settings
from .consumidor import start_consumer
import threading

class RabbitMQConsumerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.consumer_thread = threading.Thread(target=start_consumer)

    def __call__(self, request):
        if not self.consumer_thread.is_alive():
            self.consumer_thread.start()

        response = self.get_response(request)
        return response