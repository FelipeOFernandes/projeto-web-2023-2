from django.urls import path
from . import views

urlpatterns = [
    path('produtos', views.produtos, name='produtos'),
    path('produto/novo',views.cadastrarProduto,name='cadastrarProduto'),
    path('pratos',views.pratos, name='pratos'),
    path('prato/novo', views.cadastrarPrato,name='cadastrarPrato')
]