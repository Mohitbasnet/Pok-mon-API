from django.urls import path
from .views import PokemonListView

urlpatterns = [
    path('api/v1/pokemons/', PokemonListView.as_view(), name='pokemon-list'),
]
