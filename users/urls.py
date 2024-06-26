from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('chat/', views.chat, name='chat'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eventos/deletar/<int:pk>/', views.deletar_evento, name='deletar_evento'),
]
