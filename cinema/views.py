from django.shortcuts import render
from cinema.models import Movie
from rest_framework.views import APIView
from cinema.serializers import MovieListSerializer, MovieDetailSerializer
from rest_framework.response import Response
class MovieListView(APIView):

    serializer_classes = MovieListSerializer
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):

    serializer_classes = MovieDetailSerializer
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)