from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    premiere = models.BooleanField(default=False)

