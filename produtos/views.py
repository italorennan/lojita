from django.shortcuts import render
from .models import Produto
from .forms import ProdutoForm
from django.views.generic import CreateView
from django.http  import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def produtos(request):
    sitereferencia='produtos/produtos.html'
    produtos=Produto.objects.all()
    context={'produtos':produtos}
    return render(request,sitereferencia,context)

@login_required
def detalhes(request,pk):
    sitereferencia='produtos/produto_detail.html'
    produto=Produto.objects.get(pk=pk)
    context={'produto':produto}
    return render(request,sitereferencia,context)

@login_required
def produto_add(request):
    template_name = 'produtos/produto_add.html'
    return render(request,template_name)

class ProdutoCreate(CreateView):
    model = Produto
    template_name='produtos/produto_add.html'
    form_class=ProdutoForm

@login_required
def criar_produto(request):
    meuformulario=ProdutoForm
    if request.method =="POST":
        meuformulario=ProdutoForm(request.POST)
        if meuformulario.is_valid():
            print(meuformulario.cleaned_data)
            Produto.objects.create(**meuformulario.cleaned_data)
        else:
            print("Deu Erro")
    context={"form":meuformulario}
    sitereferencia="produtos/produto_add.html"
    return render(request,sitereferencia,context)

@login_required
def produto_json(request, pk):
    ''' Retorna o produto, id e estoque. '''
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})