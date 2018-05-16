from django.shortcuts import render
from django.templates import loader

# Create your views here.
def regUsuario(request):
    if request.method=="POST":
        pass
    else:
        template = loader.get_template('')
        return render(template, )