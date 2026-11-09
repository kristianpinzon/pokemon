import time
import requests
from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, Type, Ability

class Command(BaseCommand):
    help = 'Sincroniza los Pokémon hasta la novena generación desde PokéAPI'

    def add_arguments(self, parser):
        # Valor por defecto 1025 cubre hasta Gen 9 (Pecharunt #1025)
        parser.add_argument('--limit', type=int, default=1025, help='Cantidad de Pokémon a sincronizar')

    def handle(self, *args, **options):
        limit = options['limit']
        self.stdout.write(f"--- PASO 1: Descargando datos de {limit} Pokémon ---")

        species_cache = {}

        for i in range(1, limit + 1):
            url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
            species_url = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"

            try:
                res = requests.get(url, timeout=10)
                res_species = requests.get(species_url, timeout=10)

                if res.status_code != 200 or res_species.status_code != 200:
                    continue

                data = res.json()
                species_data = res_species.json()
                species_cache[data['name']] = species_data

                # Obtener nombre en español si existe
                spanish_name = data['name']
                for entry in species_data.get('names', []):
                    if entry.get('language', {}).get('name') == 'es':
                        spanish_name = entry.get('name')
                        break

                # Categoría
                category = 'normal'
                if species_data.get('is_legendary'):
                    category = 'legendary'
                elif species_data.get('is_mythical'):
                    category = 'mythical'

                # Estadísticas base
                stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}

                pokemon, _ = Pokemon.objects.update_or_create(
                    poke_id=data['id'],
                    defaults={
                        'name': data['name'],
                        'spanish_name': spanish_name,
                        'height': data['height'] / 10,
                        'weight': data['weight'] / 10,
                        'sprite_url': data['sprites']['front_default'] or '',
                        'category': category,
                        'hp': stats.get('hp', 0),
                        'attack': stats.get('attack', 0),
                        'defense': stats.get('defense', 0),
                        'special_attack': stats.get('special-attack', 0),
                        'special_defense': stats.get('special-defense', 0),
                        'speed': stats.get('speed', 0),
                    }
                )

                # Tipos
                pokemon.types.clear()
                for t_info in data['types']:
                    type_obj, _ = Type.objects.get_or_create(name=t_info['type']['name'].capitalize())
                    pokemon.types.add(type_obj)

                # Habilidades
                pokemon.abilities.clear()
                for ab_info in data['abilities']:
                    ability_obj, _ = Ability.objects.get_or_create(name=ab_info['ability']['name'].capitalize())
                    pokemon.abilities.add(ability_obj)

                self.stdout.write(self.style.SUCCESS(f"Guardado (#{pokemon.poke_id}): {spanish_name}"))
                time.sleep(0.01)

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Error de red en ID {i}: {e}"))
                time.sleep(1)

        # --- PASO 2: VÍNCULOS DE EVOLUCIÓN ---
        self.stdout.write(self.style.WARNING("\n--- PASO 2: Enlazando Cadenas Evolutivas ---"))
        
        for pokemon in Pokemon.objects.all():
            species_data = species_cache.get(pokemon.name)
            if species_data and species_data.get('evolves_from_species'):
                prev_name = species_data['evolves_from_species']['name']
                prev_pokemon = Pokemon.objects.filter(name=prev_name).first()

                if prev_pokemon:
                    pokemon.evolves_from = prev_pokemon
                    pokemon.save()
                    self.stdout.write(f"Evolución vinculada: {prev_pokemon.name} ➔ {pokemon.name}")

        self.stdout.write(self.style.SUCCESS("\n¡Sincronización completa de las 9 Generaciones finalizada con éxito!"))