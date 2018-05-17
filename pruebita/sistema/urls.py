from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('registro', views.regUsuario, name='registro'),
    path('invalido', views.login, name='invalido'),
    path('', views.opciones, name='opciones'),
    path('opciones', views.opciones, name='opciones'),
]