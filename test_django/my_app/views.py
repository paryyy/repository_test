from django.shortcuts import render
from .models import ExplainModel


# Create your views here.

def sayhello(request):
    return render(request, 'hello.html')


def explain(request):
    explains = ExplainModel.objects.all()
    context = {'explains': explains}
    return render(request, 'explain.html', context)


def Multiplication(request):
    return render(request, 'Multiplication.html')

def division(request):
    return render(request, 'division.html')