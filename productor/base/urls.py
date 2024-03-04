from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('compra', views.compra),
    path('loginpage', views.loginpage),
    path('contacto', views.contacto),
    path('trabajos', views.trabajos),
    path('home', views.home),
    path('logoutpage', views.logoutpage),
    path('perfil', views.perfil),
    path('editarperfil', views.editarperfil),
    path('registro', views.registro),
    path('reseña', views.reseña),
    path('comment/<int:id>', views.reseña),    
    path('answer/', views.answer)    
]