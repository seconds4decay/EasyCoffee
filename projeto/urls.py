"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name="home/"),
    path('home', views.home, name="home"),
    path('glossario/', views.glossario, name = "glossario/"),
    path('glossario', views.glossario, name = "glossario"),
    path('palavra/', views.palavra, name='palavra/'),
    path('palavra', views.palavra, name='palavra'),
    path('admincafe/', views.admin, name="admin/"),
    path('admincafe', views.admin, name="admin"), # Adminstração!!!
    path('produtos/', views.produtos, name="produtos/"),
    path('produtos', views.produtos, name="produtos"),
    path('buscar_cafe/', views.buscar_cafe, name='buscar_cafe'),
    path('recomendacao/', views.recomendacao, name='recomendacao'),
    path('login/', views.login, name='login/'),
    path('cadastro/', views.cadastro, name='cadastro/'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
