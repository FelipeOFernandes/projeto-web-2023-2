from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logar, name='login'),
    path('cadastro', views.registrar, name='cadastro'),
    path('logout', views.deslogar, name='logout'),
]