#from django.conf.urls import url
from django.urls import path
from  . import views



urlpatterns = [
   path('index', views.index, name='index'),
   path('contacto', views.contacto, name='contacto'),
   path('munequera', views.munequera, name='munequera'),
   path('rodillera', views.rodillera, name='rodillera'),
   path('cinturon', views.cinturon, name='cinturon'),
   path('registro', views.registro, name='registro'),
   path('checkoutV', views.checkoutV, name='checkoutV'),

   # path('listadoSQL', views.listadoSQL, name='listadoSQL'),
] 

