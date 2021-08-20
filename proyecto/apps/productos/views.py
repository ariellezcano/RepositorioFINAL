from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Producto

# Create your views here.

@login_required
def ListarProductos(request):
    # declara un diccionario que por convencion se llama context
    context = {}
    #Buscar todos los productos
    #Producto.objects.all() se transforma en:
    # SELECT * FROM Producto
    todos = Producto.objects.all() # ORM de django
    # guarda en el diccionario context los productos y se los pasa al template
    context['productos'] = todos
    # Pasarlos al template con el context al final del return para que me retorne la lista completa en el 
    # template
    return render(request, 'productos/listar.html', context)

@login_required
def DetalleProducto(request, pk):
    context = {}
    #SELECT * FROM PRODUCTOS WHERE id = pk
    objeto = Producto.objects.get(id = pk) # ORM de django
    context['producto'] = objeto
    return render(request, 'productos/detalle.html', context)

#ORM PRINCIPALES

# NOMBRE_CLASE.objects.all() "TRAE TODOS"
# NOMBRE_CLASE.objects.get() "TRAE SOLO EL QUE CUMPLA LA CONDICION"
# NOMBRE_CLASE.objects.filter() "TRAE TODOS LOS QUE CUMPLAN LA CONDICION"