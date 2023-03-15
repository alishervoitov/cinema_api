from django.urls import path
from cinema.views import MovieListView

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie')
]