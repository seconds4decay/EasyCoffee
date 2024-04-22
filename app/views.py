from django.shortcuts import render
from .models import Cafe

def home(request):
    cafes = Cafe.objects.all()
    return render(request, 'pages/home.html', {'cafes':cafes})

def glossario(request):
    return render(request, 'pages/glossario.html')

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