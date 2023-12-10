from django.shortcuts import render
from . import models

def post_view(request):
    posts = models.Post.objects.all()
    return render(request, 'post.html', {'posts': posts})