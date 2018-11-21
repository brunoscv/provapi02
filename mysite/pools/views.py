from django.shortcuts import render
from pools.models import Question

# Create your views here.

def index(request):
    return render(request, 'index.html',
                  {'questions': Question.objects.all()})

def exibir(request):
    return render(request, 'perfil.html')


