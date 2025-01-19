from django.db import models
from django.contrib.postgres.fields import JSONField


from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)  # To store the 'id' from API
    metadata = models.JSONField()  # Store all metadata in JSON format

    def __str__(self):
        return f"Movie {self.movie_id}"