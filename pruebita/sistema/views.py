from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.template import loader
from .models import Seguridad

Seguridad1 = Seguridad()

# Create your views here.
def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave = request.POST.get('pass')
        validar = Seguridad1.ingresarUsuario(usuario, clave)
        if validar == 7:
            messages.success(request,"Éxito")
            return HttpResponseRedirect('login')
        elif validar== 1:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 2:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 3:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 4:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 5:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 6:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 8:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 9:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        elif validar== 10:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('invalido')
        else:
            messages.info(request, "Error inesperado")
            return  HttpResponseRedirect('invalido')
    else:
        template = loader.get_template('prueba.html')
        return HttpResponse(template.render(None,request))

def regUsuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave1 = request.POST.get('pass')
        clave2 = request.POST.get('pass2')
        validar = Seguridad1.registrarUsuario(usuario,clave1,clave2)
        if validar == 7:
            messages.success(request,"Éxito")
            return HttpResponseRedirect('login')
        elif validar== 1:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        elif validar== 2:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        elif validar== 3:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        elif validar== 4:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        elif validar== 5:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        elif validar== 6:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        elif validar== 8:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        elif validar== 0:
            messages.info(request, Seguridad1.error[validar])
            return  HttpResponseRedirect('opciones')
        else:
            messages.info(request, "Error inesperado")
            return  HttpResponseRedirect('opciones')
    else:
        template = loader.get_template('registro.html')
        return HttpResponse(template.render(None,request))

def opciones(request):
    template = loader.get_template('opciones.html')
    return HttpResponse(template.render(None,request))