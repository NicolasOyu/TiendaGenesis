from django.shortcuts import render

from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "TiendaGenesisApp/home.html")

def informacion(request):

    return render(request, "TiendaGenesisApp/informacion.html")

def tienda(request):

    return render(request, "TiendaGenesisApp/tienda.html")

def contacto(request):

    return render(request, "TiendaGenesisApp/contacto.html")