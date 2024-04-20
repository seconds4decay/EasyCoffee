from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def glossario(request):
    return render(request, 'pages/glossario.html')