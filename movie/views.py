from django.shortcuts import render, get_object_or_404

from movie.models import Movie


def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})