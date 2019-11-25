from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    premiere = models.BooleanField(default=False)
    year = models.SmallIntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2,
                                 null=True, blank=True)
    extra_info = models.OneToOneField('ExtraInfo', on_delete=models.CASCADE,
                                      null=True, blank=True)

    def __str__(self):
        return self.title


class ExtraInfo(models.Model):
    GENRES = {
        (0, 'undefined'),
        (1, 'comedy'),
        (2, 'thriller'),
        (3, 'drama'),
        (4, 'horror'),
        (5, 'sci-fi')
    }
    genre = models.PositiveSmallIntegerField(choices=GENRES)
    duration = models.PositiveSmallIntegerField()