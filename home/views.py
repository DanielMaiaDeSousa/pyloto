from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def contato(request):
    return render(request, "contato.html")

def ajuda(request):
    return render(request, "ajuda.html")

from django.shortcuts import render
from django.http import HttpResponse

# ... outras views ...

def diasemana_view(request, dia):
    """
    Retorna o nome do dia da semana baseado no número.
    1 = Domingo, 2 = Segunda, ..., 7 = Sábado
    """
    dias = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado',
    }
    
    nome_dia = dias.get(dia, 'Dia inválido. Use um número de 1 a 7.')
    
    # Exemplo: Você pode retornar um template em vez de um HttpResponse
    return HttpResponse(f"<h1>Dia da Semana: {nome_dia}</h1>")
  