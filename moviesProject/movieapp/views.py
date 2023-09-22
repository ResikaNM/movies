from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .form import MovieForm

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    content={'movie_list':movie}
    return render(request,'index.html',content)
def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        Name=request.POST.get('name',)
        Year = request.POST.get('year',)
        Desc = request.POST.get('desc',)
        Image = request.FILES['img']
        movie=Movie(name=Name,year=Year,desc=Desc,img=Image)
        movie.save()

    return render(request, 'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


