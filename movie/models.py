from django.db import models

class Movie(models.Model):
    GENRE = [
        ('боевик', 'Боевик'),
        ('комедия', 'Комедия'),
        ('драма', 'Драма'),
        ('ужасы', 'Ужасы'),
        ('мелодрама', 'Мелодрама'),
    ]
    LANG = [
        ('английский', 'Английский'),
        ('русский', 'Русский'),
        ('французский', 'Французский'),
        ('немецкий', 'Немецкий'),
        ('испанский', 'Испанский'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    director = models.CharField(max_length=255)
    actors = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE)
    lang = models.CharField(max_length=50, choices=LANG)
    trailer_url = models.URLField()
    movie_url = models.URLField()

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)