from django.urls import path
from .views import movie_list_view, movie_detail_view, create_movie_view, delete_movie_view, update_movie_view

urlpatterns = [
    path('movies/', movie_list_view),
    path('movies/<int:id>/', movie_detail_view),
    path('movies/create/', create_movie_view),
    path('movies/<int:id>/update/', update_movie_view),
    path('movies/<int:id>/delete/', delete_movie_view),
    # path('movies/<int:id>/review/', movie_review_view)
]
