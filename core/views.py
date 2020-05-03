from django.shortcuts import render
from core.models import Evento
from django.shortcuts import redirect

# Create your views here.

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'evento': evento}
    return render(request, 'agenda.html', dados)

# def index(request):
#     return redirect('/agenda/')