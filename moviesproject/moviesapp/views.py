from django.http import HttpResponse
from django.shortcuts import render, redirect

from moviesapp.forms import Movieform
from moviesapp.models import Movies


# Create your views here.
def index(request):
    movies=Movies.objects.all()
    context={'movie_list':movies}
    return render(request,'index.html',context)
def details(request,movies_id):
    movies=Movies.objects.get(id=movies_id)
    return render(request,'details.html',{'movies':movies})
def add(request):
    if request.method=='POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        image = request.FILES['image']
        movies=Movies(name=name,desc=desc,year=year,image=image)
        movies.save()

    return render(request,'add.html')
def update(request,id):
    movie=Movies.objects.get(id=id)
    form= Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

