from django.urls import path
from .views import PokemonListCreate

urlpatterns = [
    path('api/v1/pokemons/', PokemonListCreate.as_view(), name='pokemon-list-create'),
]
