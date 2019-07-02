from django.urls import path
from .views import listaestoque,detalhesestoque,EstoqueCreate,estoque_add
app_name='estoque'

urlpatterns = [
    path('',listaestoque,name='listaestoque'),
    path('<int:pk>/',detalhesestoque,name='detalhesestoque'),
    path('add/',estoque_add,name='estoque_add'),  
    
]
