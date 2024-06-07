from django.shortcuts import render, get_object_or_404
from .models import Cafe, Palavra, favoritar
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import CafeForm
import os

from django.contrib.auth import login as lg
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


def home(request):
    cafes = Cafe.objects.all()
    user=request.user
    username=user.username

    if request.method == 'GET':
        print("OQUEI")
        print(user.username)
        if user.username == "":
            print("if 1")
            return render(request, 'pages/home.html', {'cafes':cafes, 'user': username, 'check': 0})
        elif user:
            print("if 2")
            return render(request, 'pages/home.html', {'cafes':cafes, 'user': username, 'check': 1})
        else:
            print("if 3")
            return render(request, 'pages/home.html', {'cafes':cafes, 'user': username, 'check': 0})
            
    if request.method == 'POST':
        logout(request)
        print("POST")
        return render(request, 'pages/home.html', {'cafes':cafes, 'user': username, 'check': 0})



def admin(request):
    cafes = Cafe.objects.all()
    palavras = Palavra.objects.all()
    forms = CafeForm()
    if request.method == "GET":
        return render(request, 'pages/admin.html', {'forms': forms, 'cafes':cafes, 'palavras': palavras})
    elif request.method == "POST":
        if 'removercafe' in request.POST:
            idcafe = request.POST.get('removercafe')
            cafe = Cafe.objects.filter(id_cafe=idcafe).first()
            foto = str(cafe.foto)

            atual_path = os.getcwd()
            target_file = os.path.join(atual_path, 'media/cafes', foto[6::])
            if os.path.exists(target_file):
                os.remove(target_file)

            cafe.delete()

        elif 'adicionarcafe' in request.POST:
            form = CafeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        elif 'adicionarpalavra' in request.POST:
            palavranome = request.POST.get('palavra2')
            significado = request.POST.get('significado')

            palavra = Palavra(palavra = palavranome, significado = significado)
            palavra.save()

        elif 'removerpalavra' in request.POST:
            palavranome = request.POST.get('removerpalavra')

            palavra = Palavra.objects.filter(palavra=palavranome).first()
            palavra.delete()
        
        return render(request, 'pages/admin.html', {'forms': forms, 'cafes':cafes, 'palavras': palavras})
            

def glossario(request):
    palavras = Palavra.objects.all()
    if request.method == 'GET':
        return  render(request, 'pages/glossario.html', {'palavras':palavras})

def palavra(request):
    if request.method == 'POST':
        if 'pesquisar' in request.POST:
            palavra_pesquisada = request.POST.get('palavra')
            try:
                palavra_encontrada = get_object_or_404(Palavra, palavra__iexact=palavra_pesquisada)
                return render(request, 'pages/palavra.html', {'palavra': palavra_encontrada})
            except Http404:
                # Redirecionamento para a página do glossário após 3 segundos (3000 milissegundos)
                return HttpResponse('<meta http-equiv="refresh" content="3;url=' + reverse('glossario') + '"><div style="color: red; font-size: 24px; text-align: center; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Nenhuma palavra encontrada. Redirecionando de volta ao glossário em 3 segundos...</div>')
        else:
            return HttpResponse("Parâmetro 'palavra' não fornecido na solicitação GET.")
        
def produtos(request):
    cafes = Cafe.objects.all()
    if request.method == 'GET':
        return render(request, 'pages/produtos.html', {'cafes':cafes})
    elif request.method == "POST":
        if 'tamanho' in request.POST:
            tamanhos = request.POST.getlist('tamanho')
            cafes = cafes.filter(tamanho__in=tamanhos)

        if 'intensidade' in request.POST:
            intensidades = request.POST.getlist('intensidade')
            cafes = cafes.filter(intensidade__in=intensidades)

        if 'aroma' in request.POST:
            aromas = request.POST.getlist('aroma')
            cafes = cafes.filter(aroma__in=aromas)
        
        if 'favoritar' in request.POST:
            if request.user.is_authenticated:
                id_cafe = request.POST.get('favoritar')
                user = request.user
                print(id_cafe, user)
                print('teste')
                favorito = favoritar(user=user, cafe=id_cafe)
                favorito.save()
                

            else:
                return render(request, 'pages/login.html')

        return render(request, 'pages/produtos.html', {'cafes':cafes})

def buscar_cafe(request):
    if request.method == 'POST':
        nome_pesquisado = request.POST.get('nome')
        try:
            cafe_encontrado = get_object_or_404(Cafe, nome__iexact=nome_pesquisado)
            return render(request, 'pages/cafe.html', {'cafe': cafe_encontrado})
        except Http404:
            return HttpResponse('<meta http-equiv="refresh" content="3;url=' + reverse('home') + '"><div style="color: red; font-size: 24px; text-align: center; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">Nenhum café encontrado. Redirecionando de volta à página inicial em 3 segundos...</div>')
    else:
        return HttpResponse("Parâmetro 'nome' não fornecido na solicitação POST.")
    
def recomendacao(request):
    return render(request, 'pages/recomendacao.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html', {'check': 0 })
    elif request.method == 'POST':
        if 'login' in request.POST:
            name = request.POST.get('name')
            senha = request.POST.get('senha')

            user = authenticate(request,username=name,password=senha)

            if user:
                lg(request, user)
                if request.user.is_authenticated:
                    usuario = request.user
                    username = usuario.username
                    print(usuario)
                return HttpResponseRedirect('/home/')
            else:
                print('oi')
                return render(request, 'pages/login.html',{'check': 1 } ) 
        elif 'ok' in request.POST:
                return render(request, 'pages/login.html',{'check':0 } )

def cadastro(request):
    if request.method == 'GET':
        teste="GET"
        print(teste)
        return render(request, 'pages/cadastro.html', {'check': 0, 'message':''})
    elif request.method == 'POST':
        if 'cadastrar' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            senha = request.POST.get('senha')

            user = User.objects.filter(username=name).first()

            if user:
                return render(request, 'pages/cadastro.html', {'check': 1, 'message':'Usuário já existente.'})
            else:
                user = User.objects.create_user(username=name, email=email, password=senha)
                user.save()
                return HttpResponseRedirect('/login/')
        elif 'ok' in request.POST:
            return render(request, 'pages/cadastro.html', {'check': 0, 'message':''})

def favoritos(request):
    if request.method == "GET":
        print("GET OK")
        if request.user.is_authenticated:
            print("teste")
            user=request.user
            favoritos=favoritar.objects.all()
            print(favoritos)
            
            cafes=favoritos.filter(user=user)
            return render (request, 'pages/favoritos.html', {'cafes': cafes})
        else:
            return HttpResponseRedirect('/login/')