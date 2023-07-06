#from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from  . import views



urlpatterns = [
   path('', views.index, name='index'),
   path('contacto', views.contacto, name='contacto'),
   path('munequera', views.munequera, name='munequera'),
   path('rodillera', views.rodillera, name='rodillera'),
   path('cinturon', views.cinturon, name='cinturon'),
   path('register', views.register, name='register'),
   path('checkoutV', views.checkoutV, name='checkoutV'),
   path('login', views.login, name='login'),
   path("login_user", views.login_user, name="login_user"),
   path("logout_user", views.logout_user, name="logout_user"),
   path("agregar", views.agregar, name="agregar"),
   path("modificar/<id>/", views.modificar, name="modificar"),
   path("listar", views.listar, name="listar"),
   path("eliminar/<id>/", views.eliminar, name="eliminar"),
   path("detalle/<id>/", views.detalle, name="detalle"),
   path("rodilleras", views.rodilleras, name="rodilleras"),
   path("cinturones", views.cinturones, name="cinturones"),
   path("munequeras", views.munequeras, name="munequeras"),

] 

