from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário após o registro
            return redirect('pagina_inicial')  # Substitua 'pagina_inicial' pela sua página inicial
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})