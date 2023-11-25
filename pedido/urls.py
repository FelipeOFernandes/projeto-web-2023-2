from django.urls import path
from . import views

urlpatterns = [
    path('pedir', views.pedir, name='pedir'),
    path('pedidos', views.pedidos, name='pedidos')
]