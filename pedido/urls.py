from django.urls import path
from . import views

urlpatterns = [
    path('pedir', views.pedir, name='cadastrarPedido'),
    path('', views.pedidos, name='pedidos')
]