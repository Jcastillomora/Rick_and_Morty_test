import requests

from django.shortcuts import render, HttpResponse
from .models import Personaje
# Create your views here.

def home_view(request):
    personajes = Personaje.objects.all()
    context = {"personajes": personajes}
    return render(request, template_name='core/mostrar.html', context=context)

def get_rick_data_view(request):
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        resultado = data['results']
        for dato in resultado:
            
            Personaje.objects.create(
                name=dato['name'],
                status=dato['status'],
                species=dato['species'],
                gender=dato['gender'],
                image=dato['image']
            )
        return HttpResponse("<h1> Los datos fueron cargados correctamente </h1>")
    else:
        HttpResponse("<h1> Los datos no se pudieron cargar </h1>")