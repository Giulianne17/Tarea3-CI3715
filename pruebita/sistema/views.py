from django.shortcuts import render

# Create your views here.
def menu(request):
    if request.method=="POST":
        pass
    else:
        return render(request, 'prueba.html', None)