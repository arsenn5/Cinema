from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from movie.forms import MovieForm, ReviewForms
from movie.models import Movie, Review


class MovieListView(ListView):
    queryset = Movie
    template_name = 'movies/movie_list.html'

    def get_queryset(self):
        return Movie.objects.all()


# def movie_list_view(request):
#     movies = Movie.objects.all()
#     return render(request, 'movies/movie_list.html', {'movies': movies})


# class MovieDetailView(DetailView):
#     template_name = 'movies/movie_detail.html'
#
#     def get_object(self, **kwargs):
#         movie_id = self.kwargs.get('id')
#         return get_object_or_404(Movie, id=movie_id)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        context['form'] = ReviewForms()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForms(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                content=form.cleaned_data.get('content'),
                movie=self.object
            )

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class CreateMovieView(CreateView):
    queryset = Movie.objects.all()
    form_class = MovieForm
    template_name = 'movies/movie_create.html'
    success_url = '/movies/'

    def form_valid(self, form):
        return super(CreateMovieView, self).form_valid(form=form)


# def create_movie_view(request):
#     if request.method == 'POST':
#         form = MovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен <a href="/"> На главную </a> ')
#     else:
#         form = MovieForm()
#     return render(request, 'movies/movie_create.html', {'form': form})


class UpdateMovieView(UpdateView):
    template_name = 'movies/movie_update.html'
    form_class = MovieForm
    success_url = '/movies/'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie_id)

    def form_valid(self, form):
        return super(UpdateMovieView, self).form_valid(form=form)


# def update_movie_view(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     if request.method == 'POST':
#         form = MovieForm(instance=movie, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно изменен <a href="/movies/"> На главную </a> ')
#     else:
#         form = MovieForm(instance=movie)
#     context = {
#         'form': form,
#         'movie': movie
#     }
#     return render(request, 'movies/movie_update.html', context)


class DeleteMovieView(DeleteView):
    template_name = 'movies/movie_delete.html'
    success_url = '/movies/'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie_id)


# def delete_movie_view(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     movie.delete()
#     return HttpResponse('Фильм успешно удален')


class Search(ListView):
    template_name = 'movies/movie_list.html'
    context_object_name = 'movie'
    paginate_by = 5

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
