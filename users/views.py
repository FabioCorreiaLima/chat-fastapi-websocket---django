from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import UserRegisterForm, EventoForm
from .models import Evento  # Importe o modelo Evento

# Views de autenticação e perfil
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'home.html')

# Views de eventos
@login_required  
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'users/listar_eventos.html', {'eventos': eventos})

@login_required  
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'users/criar_evento.html', {'form': form})

@login_required  
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'users/editar_evento.html', {'form': form})

@login_required  
def deletar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('profile')
    return render(request, 'users/deletar_evento.html', {'evento': evento})

@login_required
def chat(request):
    chat_server_url = "http://127.0.0.1:8001/chat/1/" + request.user.username
    return redirect(chat_server_url)

@login_required
def chat_socket_link(request):
    
    chat_server_url = "http://localhost:8001/chat/1/" + request.user.username
    return redirect(chat_server_url)
