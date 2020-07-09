from django.shortcuts import render
from django.http import HttpResponse
from .form import NameForm

def register(request):
    form = NameForm()

    return render(request, 'login.html', {'form':form})
