from django.shortcuts import render
from cinema.models import Movie
from rest_framework.views import APIView
from cinema.serializers import MovieListSerializer
from rest_framework.response import Response
class MovieListView(APIView):

    serializer_classes = MovieListSerializer
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)