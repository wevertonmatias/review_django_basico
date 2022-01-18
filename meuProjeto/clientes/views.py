from django.shortcuts import render
from django.http import HttpResponse


def clientes(request):
    return HttpResponse("Pedro, Maria, Paula")


def cliente_detalhe(request, id):
    return HttpResponse("Meu id é {}".format(id))


def cliente_detalhe_nome(request, nome):
    return HttpResponse("Meu nome é {}".format(nome))
