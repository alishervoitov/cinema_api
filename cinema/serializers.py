from rest_framework import serializers
from cinema.models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    model = Movie
    fields = [
        'title',
        'tagline',
    ]