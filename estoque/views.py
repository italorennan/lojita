from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render,resolve_url
from .models import Estoque,EstoqueItens
from .forms import EstoqueForm,EstoqueItensForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import Produto

# Create your views here.
@login_required
def listaestoque(request):
    sitereferencia='estoque/estoque.html'
    estoques=Estoque.objects.all()
    context={'estoques':estoques}
    return render(request,sitereferencia,context)

@login_required
def detalhesestoque(request,pk):
    sitereferencia='estoque/estoque_detail.html'
    estoque=Estoque.objects.get(pk=pk)
    context={'estoque':estoque}
    return render(request,sitereferencia,context)


def baixa_estoque(form):
    produtos=form.estoques.all()
    for item in produtos:
        produto=Produto.objects.get(pk=item.produto.pk)
        produto.estoque=item.saldo
        produto.save()

class EstoqueCreate(CreateView):
    model = Estoque
    template_name='estoque/estoque_add.html'
    form_class=EstoqueForm


def estoque_add(request):
    template_name='estoque/estoque_add.html'
    estoque_form=Estoque()
    item_estoque_formset=inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
        can_delete=False,
        validate_min=True,
    )
    if request.method=="POST":
        form=EstoqueForm(request.POST,instance=estoque_form,prefix='main')
        formset=item_estoque_formset(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form=form.save()
            formset.save()
            baixa_estoque(form)
            url = '/estoque/'+str(form.pk)
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form=EstoqueForm(instance=estoque_form,prefix='main')
        formset=item_estoque_formset(instance=estoque_form,prefix='estoque')
    context={'form':form,'formset':formset}
    return render(request,template_name,context)



