from django.urls import path
from .views import movie_list_view, movie_detail

urlpatterns = [
    path('movies/', movie_list_view),
    path('movies/<int:id>', movie_detail),
]