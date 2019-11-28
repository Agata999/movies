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
        fields = ['description', 'stars', 'movie']
        depth = 1

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.save()

        return instance


class MovieSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('extra_info', 'reviews')


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'premiere']


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'movies']

