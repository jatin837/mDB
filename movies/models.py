from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length = 65)
    rating = models.IntegerField()
    img_url = models.CharField(max_length = 2083)

    def __str__(self):
        return f'{self.name}'

class Actor(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(max_length = 2083)
    movies_done = models.ManyToManyField(Movie, related_name = 'actors')

    def __str__(self):
        return f'{self.name}'
