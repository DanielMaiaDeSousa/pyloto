from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Página Principal.")

def sobre(request):
    return HttpResponse("Página Sobre o sistema django.")

def contato(request):
    return HttpResponse("Página Contato do sistema django.")

def ajuda(request):
    return HttpResponse("Página Ajuda do sistema django.")  