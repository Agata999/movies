from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import UserSerializer, MovieSerializer, MovieMiniSerializer
from .models import Movie


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        movies = Movie.objects.filter(premiere=True)
        return movies

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MovieMiniSerializer(queryset, many=True)
        return Response(serializer.data)

