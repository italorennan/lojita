from django.shortcuts import render
from django.views.generic import CreateView
from produtos.models import Produto
from .models import Post

# Create your views here.

def home(request):
    context = {
        'produtos': Produto.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#def detalhes(request,pk):
#    produto=Produto.objects.get(pk=pk)
#    context = {
#        'produto' : produto
#    }
#    return render(request, 'blog/post_detail.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'content']