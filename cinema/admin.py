from django.contrib import admin
from cinema.models import Actor, Category, Genre, Movie, MovieShots, Rating, RatingStar, Reviews

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)

