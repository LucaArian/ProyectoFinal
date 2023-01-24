from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import CrearMateriasForm
from .models import Materias

# Create your views here.


def home(request):
    return render(request, "home.html")


def registrarse(request):

    if request.method == 'GET':
        return render(request, "registrarse.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                usuario = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                usuario.save()
                login(request, usuario)
                return redirect("materias")
            except IntegrityError:
                return render(request, "registrarse.html", {"form": UserCreationForm, "error": "El usuario ya existe"})

        return render(request, "registrarse.html", {"form": UserCreationForm, "error": "Las contraseñas no coinciden"})

def materias(request):
    materiasinfo = Materias.objects.all()
    return render(request, "materias.html", {"materias": materiasinfo} )


def cerrarsesion(request):
    logout(request)
    return redirect("home")

def iniciarsesion(request):
    if request.method == "GET":
        return render(request, "iniciarsesion.html", {"form":AuthenticationForm })
    else:
        usuario = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if usuario is None:
            return render(request, "iniciarsesion.html", {"form":AuthenticationForm, "error": "El usuario o la contreseña son incorrectos" })
        else:
            login(request, usuario)
            return redirect('materias')

def crear_materia(request):
    if request.method == "GET":
        return render(request, 'crear_materia.html', {"form": CrearMateriasForm})
    else:
        try:
            form = CrearMateriasForm(request.POST)
            new_materia = form.save(commit=False)
            new_materia.save()
            return redirect('materias')
        except ValueError:
            return render(request, 'crear_materias.html', {"form": CrearMateriasForm, "error": "Error creando la nueva materia."})
    

    