from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout_django
from django.contrib import messages

def registrar(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=usuario).first()
        if user:
            messages.error(request, 'Já existe um usuário com esse username.')
            return redirect('login')  # Redireciona para a página de login em caso de erro

        # se não existir usuário com esse nome, cria e salva o mesmo.
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        messages.success(request, 'Usuário criado com sucesso')

        # Autentica o usuário após o registro
        user = authenticate(request, username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('pedidos')  # Redireciona para a página de pedidos ou outra página desejada após o login

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)

        if user:
            login(request, user)
            messages.success(request, 'Login bem-sucedido!')
            return redirect('pedidos')  # Redireciona para a página de pedidos ou outra página desejada após o login
        else:
            messages.error(request, 'Usuário ou senha inválidos. Por favor, tente novamente.')
            return redirect('login')  # Redireciona para a página de login em caso de erro

    return redirect('login')

def deslogar(request):
    logout_django(request)
    messages.success(request, 'Logout bem-sucedido!')
    return redirect('login')  # Redireciona para a página de login após o logout