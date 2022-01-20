from django.contrib import admin
from .models import Cliente, Telefone, CPF, Dependente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    # fields = ['nome']
    list_display = ['id', 'nome', 'idade', 'email']
    list_filter = ['dependentes']
    search_fields = ['id', 'nome', 'dependentes__nome']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Dependente)
