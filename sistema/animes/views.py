from django.shortcuts import redirect, render
from django.http import HttpResponse
from animes.models import Anime, Serie, Pelicula
from .forms import AnimeForm, SerieForm, PeliculaForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.

        #CREO ANIME Y TODAS SUS COSAS

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

        #DEFINO ANIMES Y TODAS SUS COSAS

def animes(request):
    animes = Anime.objects.all()
    return render(request, 'animes/index.html', {'animes': animes})

def crear_anime(request):
    formulario = AnimeForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('animes')
    return render(request, 'animes/crear_anime.html', {'formulario': formulario})

def actualizar_anime(request, id):
    anime = Anime.objects.get(id=id)
    formulario = AnimeForm(request.POST or None, request.FILES or None, instance=anime)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('animes')
    return render(request, 'animes/actualizar_anime.html', {'formulario': formulario})

def borrar_anime(request, id):
    anime = Anime.objects.get(id=id)
    anime.delete()
    return render(request, 'animes')

        #CREO SERIES Y TODAS SUS COSAS

def series(request):
    series = Serie.objects.all()
    return render(request, 'series/index.html', {'series': series})

def crear_serie(request):
    formulario = SerieForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('series')
    return render(request, 'series/crear_serie.html', {'formulario': formulario})

def actualizar_serie(request, id):
    serie = Serie.objects.get(id=id)
    formulario = SerieForm(request.POST or None, request.FILES or None, instance=serie)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('series')
    return render(request, 'series/actualizar_serie.html', {'formulario': formulario})

def borrar_serie(request, id):
    serie = Serie.objects.get(id=id)
    serie.delete()
    return render(request, 'serie')

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def crear_pelicula(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/crear_pelicula.html', {'formulario': formulario})

def actualizar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/actualizar_pelicula.html', {'formulario': formulario})

def borrar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return render(request, 'pelicula')









