from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, ExtraInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['genre', 'duration']


class MovieSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)

    class Meta:
        model = Movie
        fields = ['title', 'description', 'premiere', 'year', 'rating', 'extra_info']


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'premiere']

