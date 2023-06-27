
from django.shortcuts import render
from .models import Usuario

# Create your views here.


def index(request):
    usuarios= Usuario.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'tienda/index.html', context)

def contacto(request):
    context={}
    return render(request, 'tienda/Contacto.html', context)

def rodillera(request):
    context={}
    return render(request, 'tienda/rodillera.html', context)

def munequera(request):
    context={}
    return render(request, 'tienda/munequera.html', context)

def cinturon(request):
    context={}
    return render(request, 'tienda/cinturon.html', context)

def registro(request):
    context={}
    return render(request, 'tienda/Registro.html', context)

def checkoutV(request):
    context={}
    return render(request, 'tienda/checkoutVacio.html', context)

# def listadoSQL(request):
#     alumnos= Alumno.objects.raw('SELECT * FROM alumnos_alumno')
#     print(alumnos)
#     context={"alumnos":alumnos}
#     return render(request, 'alumnos/listadoSQL.html', context)

