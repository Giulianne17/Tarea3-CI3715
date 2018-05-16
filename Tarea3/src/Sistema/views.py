from django.shortcuts import render
from django.template import loader

# Create your views here.
def regUsuario(request):
    if request.method=="POST":
        pass
    else:
        template = loader.get_template('Sistema/templates/hola.html')
        return render(request, template, None)