from django.shortcuts import render,  get_object_or_404
from .models import Cafe, Palavra
from django.http import HttpResponse


def home(request):
    cafes = Cafe.objects.all()
    return render(request, 'pages/home.html', {'cafes':cafes})

def admin(request):
    cafes = Cafe.objects.all()
    palavras = Palavra.objects.all()
    if request.method == "GET":
        return render(request, 'pages/admin.html', {'cafes':cafes, 'palavras': palavras})
    elif request.method == "POST":
        if 'removercafe' in request.POST:
            idcafe = request.POST.get('removercafe')

            cafe = Cafe.objects.filter(id_cafe=idcafe).first()
            cafe.delete()

        elif 'adicionarcafe' in request.POST:
            nomecafe = request.POST.get('cafeInput')
            descricaocafe = request.POST.get('infoInput')

            cafe = Cafe(nome=nomecafe, descricao=descricaocafe)
            cafe.save()

        elif 'adicionarpalavra' in request.POST:
            palavranome = request.POST.get('palavra2')
            significado = request.POST.get('significado')

            palavra = Palavra(palavra = palavranome, significado = significado)
            palavra.save()

        elif 'removerpalavra' in request.POST:
            palavranome = request.POST.get('removerpalavra')

            palavra = Palavra.objects.filter(palavra=palavranome).first()
            palavra.delete()
        return render(request, 'pages/admin.html', {'cafes':cafes, 'palavras': palavras})
            

def glossario(request):
    palavras = Palavra.objects.all()
    if request.method == 'GET':
        return  render(request, 'pages/glossario.html', {'palavras':palavras})
    if request.method == 'POST':
        if 'adicionar' in request.POST:
                si = request.POST.get('sig')
                pa = request.POST.get('palavra2')
                pa2 = Palavra(palavra = pa, significado = si)
                pa2.save()

                
                return  render(request, 'pages/glossario.html', {'palavras':palavras})

def palavra(request):
   
    if request.method == 'POST':

        if 'pesquisar' in request.POST:
            palavra_pesquisada = request.POST.get('palavra')
            palavra_encontrada = get_object_or_404(Palavra, palavra__iexact=palavra_pesquisada)
            return render(request, 'pages/palavra.html', {'palavra': palavra_encontrada})

        else:
            return HttpResponse("Parâmetro 'palavra' não fornecido na solicitação GET.")
        
def admin(request):
    return render(request, 'pages/admin.html')