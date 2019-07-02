from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=(
        '__str__',
        'nome',
        'preco',
        'estoque',
        'descricao',
    )
    search_fields=('nome',)
# Register your models here.
