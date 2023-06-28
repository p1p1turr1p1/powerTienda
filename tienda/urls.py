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

   # path('listadoSQL', views.listadoSQL, name='listadoSQL'),
] 

