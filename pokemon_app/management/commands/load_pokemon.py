import requests
from django.core.management.base import BaseCommand
from pokemon_app.models import Pokemon

class Command(BaseCommand):
    help = 'Load Pokémon data from PokeAPI'

    def handle(self, *args, **kwargs):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
        if response.status_code == 200:
            data = response.json()
            for pokemon in data['results']:
                pokemon_data = requests.get(pokemon['url']).json()
                types = ', '.join(t['type']['name'] for t in pokemon_data['types'])
                Pokemon.objects.create(
                    name=pokemon_data['name'],
                    image=pokemon_data['sprites']['front_default'],
                    types=types
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded Pokémon data'))
