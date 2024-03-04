from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Planes (models.Model):
    title = models.CharField (max_length = 30)
    info = models.TextField()
    price = models.CharField (max_length = 30)

    def __str__(self):
        return self.title

class Mensaje (models.Model):
    nombre = models.CharField (max_length = 50)
    email = models.CharField (max_length = 100)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
        
    
class Perfil (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField (max_length = 50)
    apellido = models.CharField (max_length = 50)
    email = models.CharField (max_length = 50)

    def __str__(self):
        return (self.nombre + self.apellido) 

class Reseña (models.Model):
    first_name = models.CharField (max_length = 50)
    comment = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 
    
    def __str__(self):
        return self.first_name
    
class Answer(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    comment = models.ForeignKey(Reseña , on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    