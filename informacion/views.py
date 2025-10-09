from django.shortcuts import render

def informacion(request):

    return render(request, "informacion/informacion.html")

