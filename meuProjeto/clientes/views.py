from django.shortcuts import render
from django.http import HttpResponse


def clientes(request):
    data = {
        "clientes": [
            {"nome": "Pedro", "idade": 25},
            {"nome": "Filomena", "idade": 56},
            {"nome": "Pororo", "idade": 41}
        ]
    }
    return render(request, 'clientes/index.html', data)
    # return HttpResponse("Pedro, Maria, Paula")


def cliente_detalhe(request, id):
    return HttpResponse("Meu id é {}".format(id))


def cliente_detalhe_nome(request, nome):
    return HttpResponse("Meu nome é {}".format(nome))
