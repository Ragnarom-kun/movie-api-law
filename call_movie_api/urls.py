from django.urls import path
from .views import MovieList, MovieSearch

urlpatterns = [
    path('list/', MovieList.as_view()),
    path('search/', MovieSearch.as_view()),
]