from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from movie.forms import MovieForm
from movie.models import Movie, Review


def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


def movie_detail_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


def create_movie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен <a href="/"> На главную </a> ')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_create.html', {'form': form})


def update_movie_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieForm(instance=movie, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно изменен <a href="/movies/"> На главную </a> ')
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie
    }
    return render(request, 'movies/movie_update.html', context)

def delete_movie_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return HttpResponse('Фильм успешно удален')