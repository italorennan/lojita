from django.urls import path
from .views import home, PostCreateView #, detalhes

urlpatterns = [
    path('', home, name='home'),
    #path('post/<int:pk>/', detalhes, name='post-detail'),
    path('comentario/novo', PostCreateView.as_view(), name='post-create'),
]