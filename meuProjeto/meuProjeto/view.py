from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá mundo")


def clientes(request):
    return HttpResponse("Pedro, Maria, Paula")


def cliente_detalhe(request, id):
    return HttpResponse("Meu id é {}".format(id))


def cliente_detalhe_nome(request, nome):
    return HttpResponse("Meu nome é {}".format(nome))
