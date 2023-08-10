"""
URL configuration for django_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import tienda_virtual.views as views


#Cosas Nuevas y raras
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loading),
    path('home', views.home),
    path('signin', views.signin),
    path('signup', views.signup),
    path('signout', views.signout),
    path('account', views.seeaccount),
    path('productos', views.shop),
    path('productos/<int:objetID>', views.seearticle),
    path('car', views.seeCarrito),
    path('search', views.search)
]

#cosas nuevas y raras
urlpatterns += staticfiles_urlpatterns()