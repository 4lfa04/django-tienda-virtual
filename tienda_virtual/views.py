from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Wallet, Message, Objeto
import random
import django.contrib.staticfiles
from django.contrib.auth.decorators import login_required


# Create your views here.
def loading(req):
    return render(req, 'loading.html')

def home(req):
    mensajes = checkMessage(req, req.user)
    print(mensajes)
    return render(req, 'home.html',{
        'messages': mensajes
    })



def signin(req):
    if req.method == 'GET':
        return render(req, 'signin.html')
    else:
        # print(req.POST['username'])
        user = authenticate(req, username=req.POST['username'], password=req.POST['password'])
        if user is None:
            return render(req, 'signin.html', {
            'error': 'Nombre de usuario o contraseña incorrectos'
        })
        else:
            login(req, user)
            return redirect('/home')
        
def signup(req):
    if req.method == 'GET':
        return render(req, 'signup.html')
    else:
        try:
            user = User.objects.create_user(username=req.POST['username'], password=req.POST['password1'])
            user.save()
            login(req, user)
            createWallet(req, user)
            Message.objects.create(user=user,message='wallet_created')
            # return redirect('/home')
            return redirect('/home')
            # return render(req, 'home.html', {
            #     'mensaje':'wallet_created'
            # })
        except:
            return render(req, 'signup.html', {
                'error': 'Esta Cuenta ya existe, por favor elija otra'
            })
    
@login_required    
def signout(req):
    logout(req)
    return redirect('/home')

@login_required
def seeaccount(req):
    var = Wallet.objects.get(user=req.user)
    return render(req, 'account.html', {
        'secret_wallet': var.wallet,
        'cash': var.cash
    })
    
@login_required
def shop(req):
    objetos = Objeto.objects.all()
    return render(req, 'shop.html',{
        'objetos':objetos
    })

@login_required
def seearticle(req, objetID):
    if req.method == 'GET':
        objeto = Objeto.objects.get(pk=objetID)
        wallet = Wallet.objects.get(user=req.user)
        cantidad = 0
        try:
            for articulo in wallet.carrito:
                if articulo['objeto'] == objeto.objeto:
                    cantidad = articulo['cantidad']
                    print(articulo)
            
            return render(req, 'article.html',{
                'objeto': objeto,
                'cantidad':cantidad
            })
        except:
            return render(req, 'article.html',{
                'objeto': objeto,
                'cantidad':cantidad
            })
            
    else:
        objeto = Objeto.objects.get(pk=objetID)
        cantidad = 0
        wallet = Wallet.objects.get(user=req.user)
        carrito = wallet.carrito
        modeloCarrito = []
        try:
            artLista = []
            if wallet.carrito != None:
                for a in wallet.carrito:
                    artLista.append(a['objeto'])
            if wallet.carrito == None or wallet.carrito == []:
                modeloCarrito.append({
                    'pk': objeto.pk,
                    'objeto':objeto.objeto,
                    'foto':objeto.foto,
                    'precio':objeto.precio,
                    'cantidad':req.POST['cantidad']
                })
                wallet.carrito = modeloCarrito
                wallet.save()
            elif req.POST['articulo'] in artLista:
                for articulo in wallet.carrito:
                    b = articulo
                    if req.POST['articulo'] == articulo['objeto']:
                        b['cantidad'] = req.POST['cantidad']
                    modeloCarrito.append(b)
                wallet.carrito = modeloCarrito
                wallet.save()
            elif req.POST['articulo'] not in artLista:
                for articulo in wallet.carrito:
                    c = articulo
                    modeloCarrito.append(c)
                modeloObjeto = {
                    'pk': objeto.pk,
                    'objeto':objeto.objeto,
                    'foto':objeto.foto,
                    'precio':objeto.precio,
                    'cantidad':req.POST['cantidad']
                }
                modeloCarrito.append(modeloObjeto)
                wallet.carrito = modeloCarrito
                wallet.save()
        except Exception as e:
            print(f'Error: {e}')
        
        return redirect('/car')
        
@login_required
def seeCarrito(req):
    stock = Objeto.objects.all()
    carrito = Wallet.objects.get(user=req.user)
    try:
        total = calcularPreciototal(req,carrito.carrito)    
        return render(req, 'carrito.html',{
            'objetos': carrito.carrito,
            'total': total
        })
    except:
        return render(req, 'carrito.html',{
            'objetos': carrito.carrito,
            'total': 0
        })
    
 
# Funciones Agregadas

def createWallet(req, user):
    letras = ['1','2','3','4','5','6','7','8','9','0']
    lista = [random.choice(letras) for i in range(8)]
    wallet = ''
    for i in range(8):
        wallet = wallet + lista[i-1]
    createdWallets = Wallet.objects.all()
    if wallet in createdWallets:
        return createWallet()
    else:
        Wallet.objects.create(user=user,wallet=wallet,cash=5)
        
def checkMessage(req, user):
    try:
        mensaje = Message.objects.get(user=user)
        k = mensaje
        k = str(k.message)
        mensaje.message = 'empty'
        mensaje.save()
        return k
    except Exception as e:
        print(e)
        return 'new_user'
    
def calcularPreciototal(req,lista):
    total = 0
    for i in lista:
        cant = int(i['cantidad'])
        price = int(i['precio'])
        total += cant*price
    return total

def search(req):
    print(req)
    return HttpResponse('buscando')