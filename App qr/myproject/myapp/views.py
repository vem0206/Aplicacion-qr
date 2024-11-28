
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from . import qrcode  

def index(request):
    """
    Renderiza la página principal con el botón START.
    """
    return render(request, 'index.html')

def start_qrcode(request):
    """
    Llama a la función de lectura QR en qrcode.py.
    """
    if request.method == "POST":
        qrcode.main()  
    return redirect('index')  

def register(request):
    """
    Maneja el registro de nuevos usuarios.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            username = form.cleaned_data.get('username')
            messages.success(request, f"¡Cuenta creada para {username}!")
            return redirect('index')  # Redirige a la página principal después del registro
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


