from django.urls import path
from informacion import views

urlpatterns = [

    path('', views.informacion, name = "Informacion"),
    
]