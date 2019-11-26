from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, ExtraInfo, Review, Actor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['genre', 'duration']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['description', 'stars']


class MovieSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['title', 'description', 'premiere', 'year', 'rating', 'extra_info', 'reviews']


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'premiere']


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieMiniSerializer(many=True)

    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'movies']

