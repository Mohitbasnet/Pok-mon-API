from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer
from django.conf import settings
import requests

class PokemonListCreate(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        types = self.request.query_params.get('types')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        if types:
            queryset = queryset.filter(types__icontains=types)
        
        return queryset

    def perform_create(self, serializer):
        if Pokemon.objects.count() == 0:
            response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')
            pokemons = response.json().get('results', [])
            
            for pokemon in pokemons:
                details = requests.get(pokemon['url']).json()
                name = details['name']
                image = details['sprites']['front_default']
                types = ', '.join(t['type']['name'] for t in details['types'])
                Pokemon.objects.create(name=name, image=image, types=types)
        
        super().perform_create(serializer)
