from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Actor

def index(request):
    context = {
        'movies':Movie.objects.all()
    }
    return render(request, 'index.html', context)
def details(request, id):
    return render(request, 'detail.html', {"movie":Movie.objects.get(id = id), 'actors': Movie.objects.get(id = id).actors.all()})

#def getName(request):
#    if request.method == "POST":
#        form = NameForm(request.POST)
#        if form.is_valid():
#            return HttpResponse('It works')
#
#    else :
#        form = NameForm()
#        return render(request, 'test.html', {'form':form})
