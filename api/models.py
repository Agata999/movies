from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


for user in User.objects.all():
    Token.objects.get_or_create(user=user)


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    premiere = models.BooleanField(default=False)
    year = models.SmallIntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    extra_info = models.OneToOneField(
        "ExtraInfo", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title


class ExtraInfo(models.Model):
    GENRES = {
        (0, "undefined"),
        (1, "comedy"),
        (2, "thriller"),
        (3, "drama"),
        (4, "horror"),
        (5, "sci-fi"),
    }
    genre = models.PositiveSmallIntegerField(choices=GENRES)
    duration = models.PositiveSmallIntegerField()


class Review(models.Model):
    description = models.TextField()
    stars = models.PositiveSmallIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")


class Actor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    movies = models.ManyToManyField(Movie)
