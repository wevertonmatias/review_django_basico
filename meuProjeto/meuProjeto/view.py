from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo = "F"
    nome = "Carla"
    data = {
        "primeiro_nome": nome,
        "sexo": sexo
    }
    return render(request, 'index.html', data)
