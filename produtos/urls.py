from django.urls import path
from .views import produtos,detalhes,criar_produto,produto_json

app_name='produtos'

urlpatterns = [
    path('',produtos),
    path('<int:pk>/',detalhes,name='detalhes'),  
    path('add/',criar_produto,name='produto_add'),
    path('<int:pk>/json/',produto_json, name='produto_json'),
]

# //request > urls > view > model > response s