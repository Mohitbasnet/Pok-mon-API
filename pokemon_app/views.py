from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pokemon
from .serializers import PokemonSerializer
from .filters import PokemonFilter

class PokemonListView(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PokemonFilter
