from django.db import models


class ParserModel(models.Model):
    title_name = models.CharField(max_length=100)
    title_url = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.title_name}'
