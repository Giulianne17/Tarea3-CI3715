from django.shortcuts import render
from django.template import loader

# Create your views here.
def regUsuario(request):
    if request.method=="POST":
        pass
    else:
        template = loader.get_template('templates/Sistema/index.html')
        return render(template)