from django.urls import path
from .views import clientes, cliente_detalhe, cliente_detalhe_nome

urlpatterns = [
    path('', clientes),
    path('cliente/<int:id>', cliente_detalhe),
    path('cliente_nome/<str:nome>', cliente_detalhe_nome),
]
