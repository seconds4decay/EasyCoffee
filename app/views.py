from django.shortcuts import render,  get_object_or_404
from .models import Cafe, Palavra
from django.http import HttpResponse


def home(request):
    cafes = Cafe.objects.all()
    return render(request, 'pages/home.html', {'cafes':cafes})

def adicionarcafe(request):
    cafes = Cafe.objects.all()
    if request.method == "GET":
        return render(request, 'pages/adicionarcafe.html', {'cafes':cafes})
    elif request.method == "POST":
        if 'remover' in request.POST:
            idcafe = request.POST.get('remover')

            cafe = Cafe.objects.filter(id_cafe=idcafe).first()
            cafe.delete()
        else:
            nomecafe = request.POST.get('cafeInput')
            descricaocafe = request.POST.get('infoInput')

            cafe = Cafe(nome=nomecafe, descricao=descricaocafe)
            cafe.save()
        return render(request, 'pages/adicionarcafe.html', {'cafes':cafes})
    

def glossario(request):
    if request.method == 'GET':
        return  render(request, 'pages/glossario.html')
    if request.method == 'POST':
        if 'adicionar' in request.POST:
                si = request.POST.get('sig')
                pa = request.POST.get('palavra2')
                pa2 = Palavra(palavra = pa, significado = si)
                pa2.save()
                return  render(request, 'pages/glossario.html')

def palavra(request):
   
    if request.method == 'POST':

        if 'pesquisar' in request.POST:
            palavra_pesquisada = request.POST.get('palavra')
            palavra_encontrada = get_object_or_404(Palavra, palavra__iexact=palavra_pesquisada)
            return render(request, 'pages/palavra.html', {'palavra': palavra_encontrada})

        else:
            return HttpResponse("Parâmetro 'palavra' não fornecido na solicitação GET.")