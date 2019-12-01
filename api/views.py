from django.contrib.auth.models import User
from django.http.response import HttpResponseNotAllowed
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    MovieSerializer,
    MovieMiniSerializer,
    ReviewSerializer,
    ActorSerializer,
)
from .models import Movie, Review, Actor


class MoviesSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 7


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    filterset_fields = [
        "title",
    ]
    search_fields = ["title", "description"]
    ordering_fields = "__all__"
    pagination_class = MoviesSetPagination

    def get_queryset(self):
        movies = Movie.objects.filter(premiere=True)
        return movies

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            movie = Movie.objects.create(
                title=request.data["title"],
                description=request.data["description"],
                premiere=request.data["premiere"],
                year=request.data["year"],
            )
            serializer = MovieMiniSerializer(movie, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed("Not allowed")

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            movie = self.get_object()
            movie.title = request.data["title"]
            movie.description = request.data["description"]
            movie.premiere = request.data["premiere"]
            movie.year = request.data["year"]
            movie.save()
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed("Not allowed")

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            movie = self.get_object()
            movie.delete()
            return Response("Movie deleted")
        else:
            return HttpResponseNotAllowed("Not allowed")

    @action(detail=True)
    def premiere(self, request, **kwargs):
        movie = self.get_object()
        movie.premiere = True
        movie.save()
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=True, methods=["post"])
    def append_movie(self, request, **kwargs):
        actor = self.get_object()
        movie = Movie.objects.get(id=request.data["movies"])
        actor.movies.add(movie)
        serializer = ActorSerializer(actor, many=False)
        return Response(serializer.data)
