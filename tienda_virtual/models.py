from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=8)
    # carrito = models.CharField(max_length=1000, null=True, blank=True)
    carrito = models.JSONField(null=True, blank=True)
    cash = models.IntegerField(null=True)
    
    def __str__(self):
        return f'Wallet: {self.user}'
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.JSONField(default=None)
    
    def __str__(self):
        return f'Messages of {self.user}'
    
class Objeto(models.Model):
    objeto = models.CharField(max_length=50)
    precio = models.IntegerField(null=True)
    propietario = models.CharField(max_length=50, null=True, blank=True)
    foto = models.CharField(max_length=500, null=True, blank=True)
    etiquetas = models.CharField(max_length=500, null=True, blank=True)
        
    def __str__(self):
        return self.objeto