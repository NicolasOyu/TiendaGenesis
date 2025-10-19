from django.shortcuts import render
from .models import Producto, CategoriaProducto

# Create your views here.

def tienda(request):

    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.all()

    return render(request, "tienda/tienda.html", {
        "productos": productos,
        "categorias": categorias
    })

def categoria(request, categoria_id):
    categoria = CategoriaProducto.objects.get(id=categoria_id)  # Usa id o el nombre correcto del campo
    productos = Producto.objects.filter(categoria=categoria)  # Filtrar por FK

    return render(request, "tienda/categorias.html", {
        "categoria": categoria,
        "productos": productos
    })
