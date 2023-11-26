from django.urls import path
from . import views

urlpatterns = [
    path('produtos', views.produtos, name='produtos'),
    path('produto/criar',views.cadastrarProduto,name='cadastrarProduto'),
    path('produto/editar/<id>',views.editarProduto,name='editarProduto'),
    path('produto/deletar/<id>',views.deletarProduto,name='deletarProduto'),
    path('pratos',views.pratos, name='pratos'),
    path('prato/novo', views.cadastrarPrato,name='cadastrarPrato')
]