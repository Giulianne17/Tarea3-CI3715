from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.regUsuario, name="registro_usuario")
]