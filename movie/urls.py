from django.urls import path
from .views import MovieListView, MovieDetailView, CreateMovieView, DeleteMovieView, UpdateMovieView, Search

# from .views import movie_list_view, movie_detail_view, create_movie_view, delete_movie_view, update_movie_view
#
# urlpatterns = [
#     path('movies/', movie_list_view),
#     path('movies/<int:id>/', movie_detail_view),
#     path('movies/create/', create_movie_view),
#     path('movies/<int:id>/update/', update_movie_view),
#     path('movies/<int:id>/delete/', delete_movie_view),
# ]

urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/', MovieDetailView.as_view()),
    path('movies/create/', CreateMovieView.as_view()),
    path('movies/<int:id>/update/', UpdateMovieView.as_view()),
    path('movies/<int:id>/delete/', DeleteMovieView.as_view()),
    path('search/', Search.as_view(), name='search'),
]