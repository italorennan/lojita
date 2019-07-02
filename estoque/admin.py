from django.contrib import admin
from .models import Estoque,EstoqueItens,TimeStampedModel
# Register your models here.

class EstoqueItensInline(admin.TabularInline):
    model=EstoqueItens
    extra=0

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    inlines=(EstoqueItensInline,)
    list_display=('__str__','notafiscal')
    list_filter=('funcionario',)
    date_hierarchy='created'
    

