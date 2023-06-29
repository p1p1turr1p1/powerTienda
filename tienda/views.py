
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Producto
from .forms import ProductoForm


# Create your views here.


def index(request):
    productos = Producto.objects.all()
    context={'productos': productos}
    return render(request, 'tienda/index.html', context)

def contacto(request):
    context={}
    return render(request, 'tienda/Contacto.html', context)

def rodillera(request):
    context={}
    return render(request, 'tienda/rodill era.html', context)

def munequera(request):
    context={}
    return render(request, 'tienda/munequera.html', context)

def cinturon(request):
    context={}
    return render(request, 'tienda/cinturon.html', context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Ya existe una cuenta con esos datos.')
                return redirect(register) 
            else:
                user = User.objects.create_user(username=username,
password=password, email=email, first_name=first_name, last_name=last_name) 
                user.set_password(password) 
                user.save()
                print("funka")
                return redirect('login_user')
        else:
            messages.info(request, 'No coinciden las contraseñas')
            return redirect(register)
    else:
        print("no post method")
        return render(request, 'tienda/register.html')
                                    
def login_user(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'tienda/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('index')

def checkoutV(request):
    context={}
    return render(request, 'tienda/checkoutVacio.html', context)

def login(request):
    context={}
    return render(request, 'tienda/login.html', context)

def agregar(request):
    context={'form': ProductoForm}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            context["mensaje"] = "guardado correctamente"
        else:
            context["form"] = formulario
        
    return render(request, 'tienda/agregar.html', context)

def listar(request):
    productos = Producto.objects.all()
    context={'productos':productos}
    return render(request, 'tienda/listar.html', context)


def modificar(request, id):
    producto = get_object_or_404(Producto, id=id)
    context={'form': ProductoForm(instance=producto)}
    if request.method == 'POST':
        formulario = ProductoForm (data=request. POST, instance=producto, files=request. FILES)
        if formulario.is_valid():
            formulario. save ()
            return redirect (to="listar")
        context["form"] | formulario
    return render(request, 'tienda/modificar.html', context)

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect (to="listar")
