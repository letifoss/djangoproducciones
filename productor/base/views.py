from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Planes
from .models import Mensaje
from .models import Perfil
from .models import Reseña
from .models import Answer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

from django.views.decorators.csrf import csrf_protect

@csrf_protect

# Create your views here.


def home(request):
    reseña = Reseña.objects.all()
    return render(request, 'home.html', {'reseña': reseña})

def compra(request):
    planes = Planes.objects.all()
    return render(request, 'compra.html', {'planes': planes} )
    

def loginpage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inició sesión correctamente')
                return redirect('/')
        messages.error(request, 'Correo electronico o contraseña incorrectos')
    return render(request, 'loginpage.html' )

def logoutpage(request):
    logout(request)
    return redirect('/')


def contacto(request):
    if request.method == 'POST':
        Mensaje.objects.create(
            nombre = request.POST.get('nombre'),
            email = request.POST.get('email'),
            mensaje = request.POST.get('mensaje')
        )
        messages.success(request, 'Mensaje enviado correctamente')
    return render(request, 'contacto.html')

def trabajos(request):
    return render(request, 'trabajos.html' )


def perfil(request):
    return render(request, 'perfil.html' )

def editarperfil(request):
    return render(request, 'editarperfil.html' )


def registro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/registro')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Ya existe un usuario con este correo electrónico.')
            return redirect('/registro')

        # Crea el nuevo usuario y asocia el perfil
        new_user = User.objects.create_user(username=email, email=email, password=password,
                                            first_name=first_name, last_name=last_name)

        Perfil.objects.create(
            user=new_user, nombre=first_name, apellido=last_name, email=email
        )

        messages.success(request, 'Cuenta creada correctamente, inicia sesión para acceder')
        return redirect('/loginpage')

    return render(request, 'registro.html', {'perfil': perfil})


def reseña(request, id=None):
    if request.method == 'POST':
        if id is None:
            first_name = request.POST.get('first_name')
            comment = request.POST.get('comment')
            Reseña.objects.create(first_name=first_name, comment=comment, user=request.user)
            messages.success(request, 'Gracias por tu comentario :) ')
        else:
            p = get_object_or_404(Reseña, id=id)
            if (p.user == request.user):
                p.first_name = request.POST.get('first_name')
                p.comment = request.POST.get('comment')
                p.save()
                messages.success(request, 'Comentario modificado ')

    context = {}
    if id is not None:
        p = get_object_or_404(Reseña, id=id)
        context['reseña'] = p

    return render(request, 'reseña.html', context)


def answer(request):
    p = Reseña.objects.get(id = request.POST.get('comment'))
    Answer.objects.create(
        text=request.POST.get('text'),
        user=request.user,
        comment = p 
    )
    return redirect('/')