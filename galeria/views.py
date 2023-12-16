from django.shortcuts import render

# O segundo argumento do render está ligado a pasta templates

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')