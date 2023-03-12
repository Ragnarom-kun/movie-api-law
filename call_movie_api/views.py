import requests
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class MovieList(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=1885b67f5e72121ad8e87eb11b290abe')
        movies = response.json()['results']
        return [Movie(title=m['title'], overview=m['overview'], poster_path=m['poster_path']) for m in movies]
    
class MovieSearch(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if not query:
            return Response({'error': 'Please provide a search query.'})

        api_key = '1885b67f5e72121ad8e87eb11b290abe'
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
        response = requests.get(url)
        results = response.json()['results']

        # Process the movie results and return them in the response
        movies = []
        for result in results:
            movie = {
                'title': result['title'],
                'release_date': result['release_date'],
                'poster_path': result['poster_path'],
                'overview': result['overview']
            }
            movies.append(movie)

        return Response({'results': movies})
