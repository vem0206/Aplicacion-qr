from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),           # Página principal
    path('start/', views.start_qrcode, name='start_qrcode'),  # Lector QR
    path('register/', views.register, name='register'),       # Registro de usuario
]




