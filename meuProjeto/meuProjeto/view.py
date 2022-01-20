from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    nome = "Patata"
    data = {
        "primeiro_nome" : nome
    }
    return render(request, 'index.html', data)
