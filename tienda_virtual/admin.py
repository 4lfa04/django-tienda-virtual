from django.contrib import admin
from .models import Wallet, Message, Objeto

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Message)
admin.site.register(Objeto)