from django.urls import path
from cinema.views import MovieListView, MovieDetailView,ReviewCreateView

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('review/', ReviewCreateView.as_view(), name='review'),
]