import django_filters
from .models import Pokemon

class PokemonFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    types = django_filters.CharFilter(field_name='types', lookup_expr='icontains')

    class Meta:
        model = Pokemon
        fields = ['name', 'types']
