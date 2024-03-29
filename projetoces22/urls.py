from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('produtos/', include('produtos.urls')),
    path('estoque/', include('estoque.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('cadastrar/', user_views.cadastrar, name='cadastrar'),
    path('', include('blog.urls')),
]