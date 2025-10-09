from django.urls import path
from TiendaGenesisApp import views

urlpatterns = [

    path('', views.home, name = "Inicio"),
    path('tienda', views.tienda, name = "Tienda"),
    path('informacion', views.informacion, name = "Informacion"),
    path('contacto', views.contacto, name = "Contacto"),
    
]