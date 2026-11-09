
from django.core.management.base import BaseCommand
from pokedex.models import Region, Gym, Type


class Command(BaseCommand):
    help = 'Pobla las 9 regiones con sus gimnasios y medallas'

    def handle(self, *args, **options):

        # 9 Regiones completas
        regions_data = [
            {'name': 'Kanto', 'gen': 1, 'prof': 'Profesor Oak'},
            {'name': 'Johto', 'gen': 2, 'prof': 'Profesor Elm'},
            {'name': 'Hoenn', 'gen': 3, 'prof': 'Profesor Birch'},
            {'name': 'Sinnoh', 'gen': 4, 'prof': 'Profesor Rowan'},
            {'name': 'Teselia / Unova', 'gen': 5, 'prof': 'Profesora Juniper'},
            {'name': 'Kalos', 'gen': 6, 'prof': 'Profesor Sycamore'},
            {'name': 'Alola', 'gen': 7, 'prof': 'Profesor Kukui'},
            {'name': 'Galar', 'gen': 8, 'prof': 'Profesora Magnolia'},
            {'name': 'Paldea', 'gen': 9, 'prof': 'Profesora Sada / Profesor Turo'},
        ]

        # Registrar las regiones
        for r in regions_data:
            Region.objects.update_or_create(
                name=r['name'],
                defaults={
                    'generation': r['gen'],
                    'professor': r['prof']
                }
            )

        # Gimnasios de las regiones
        gyms_data = [

            # Gen 1 - Kanto
            {'region': 'Kanto', 'town': 'Ciudad Plateada', 'leader': 'Brock', 'badge': 'Roca', 'type': 'Roca'},
            {'region': 'Kanto', 'town': 'Ciudad Celeste', 'leader': 'Misty', 'badge': 'Cascada', 'type': 'Agua'},
            {'region': 'Kanto', 'town': 'Ciudad Carmín', 'leader': 'Lt. Surge', 'badge': 'Trueno', 'type': 'Eléctrico'},
            {'region': 'Kanto', 'town': 'Ciudad Azulona', 'leader': 'Erika', 'badge': 'Arcoíris', 'type': 'Planta'},
            {'region': 'Kanto', 'town': 'Ciudad Fucsia', 'leader': 'Koga', 'badge': 'Alma', 'type': 'Veneno'},
            {'region': 'Kanto', 'town': 'Ciudad Azafrán', 'leader': 'Sabrina', 'badge': 'Pantano', 'type': 'Psíquico'},
            {'region': 'Kanto', 'town': 'Isla Canela', 'leader': 'Blaine', 'badge': 'Volcán', 'type': 'Fuego'},
            {'region': 'Kanto', 'town': 'Ciudad Verde', 'leader': 'Giovanni', 'badge': 'Tierra', 'type': 'Tierra'},

            # Gen 2 - Johto
            {'region': 'Johto', 'town': 'Ciudad Malva', 'leader': 'Falkner', 'badge': 'Céfiro', 'type': 'Volador'},
            {'region': 'Johto', 'town': 'Pueblo Azalea', 'leader': 'Bugsy', 'badge': 'Colmena', 'type': 'Bicho'},
            {'region': 'Johto', 'town': 'Ciudad Trigal', 'leader': 'Whitney', 'badge': 'Llanura', 'type': 'Normal'},
            {'region': 'Johto', 'town': 'Ciudad Iris', 'leader': 'Morty', 'badge': 'Niebla', 'type': 'Fantasma'},
            {'region': 'Johto', 'town': 'Ciudad Orquídea', 'leader': 'Chuck', 'badge': 'Tormenta', 'type': 'Lucha'},
            {'region': 'Johto', 'town': 'Ciudad Olivo', 'leader': 'Jasmine', 'badge': 'Mineral', 'type': 'Acero'},
            {'region': 'Johto', 'town': 'Pueblo Caoba', 'leader': 'Pryce', 'badge': 'Glaciar', 'type': 'Hielo'},
            {'region': 'Johto', 'town': 'Ciudad Endrina', 'leader': 'Clair', 'badge': 'Dragón', 'type': 'Dragón'},

            # Gen 3 - Hoenn
            {'region': 'Hoenn', 'town': 'Ciudad Férrica', 'leader': 'Roxanne', 'badge': 'Piedra', 'type': 'Roca'},
            {'region': 'Hoenn', 'town': 'Ciudad Portual', 'leader': 'Brawly', 'badge': 'Puño', 'type': 'Lucha'},
            {'region': 'Hoenn', 'town': 'Ciudad Malvalona', 'leader': 'Wattson', 'badge': 'Dinamo', 'type': 'Eléctrico'},
            {'region': 'Hoenn', 'town': 'Pueblo Lavacalda', 'leader': 'Flannery', 'badge': 'Calor', 'type': 'Fuego'},
            {'region': 'Hoenn', 'town': 'Ciudad Petalia', 'leader': 'Norman', 'badge': 'Equilibrio', 'type': 'Normal'},
            {'region': 'Hoenn', 'town': 'Ciudad Arborada', 'leader': 'Winona', 'badge': 'Pluma', 'type': 'Volador'},
            {'region': 'Hoenn', 'town': 'Ciudad Algaria', 'leader': 'Tate y Liza', 'badge': 'Mente', 'type': 'Psíquico'},
            {'region': 'Hoenn', 'town': 'Arrecípolis', 'leader': 'Juan / Wallace', 'badge': 'Lluvia', 'type': 'Agua'},

            # Gen 4 - Sinnoh
            {'region': 'Sinnoh', 'town': 'Ciudad Pirita', 'leader': 'Roark', 'badge': 'Carbón', 'type': 'Roca'},
            {'region': 'Sinnoh', 'town': 'Ciudad Vetusta', 'leader': 'Gardenia', 'badge': 'Bosque', 'type': 'Planta'},
            {'region': 'Sinnoh', 'town': 'Ciudad Rocaveloz', 'leader': 'Maylene', 'badge': 'Adoquín', 'type': 'Lucha'},
            {'region': 'Sinnoh', 'town': 'Ciudad Pradera', 'leader': 'Crasher Wake', 'badge': 'Ciénaga', 'type': 'Agua'},
            {'region': 'Sinnoh', 'town': 'Ciudad Corazón', 'leader': 'Fantina', 'badge': 'Reliquia', 'type': 'Fantasma'},
            {'region': 'Sinnoh', 'town': 'Ciudad Canalave', 'leader': 'Byron', 'badge': 'Mina', 'type': 'Acero'},
            {'region': 'Sinnoh', 'town': 'Ciudad Puntaneva', 'leader': 'Candice', 'badge': 'Carámbano', 'type': 'Hielo'},
            {'region': 'Sinnoh', 'town': 'Ciudad Marina', 'leader': 'Volkner', 'badge': 'Faro', 'type': 'Eléctrico'},

            # Gen 5 - Teselia / Unova
            {'region': 'Teselia / Unova', 'town': 'Ciudad Gres', 'leader': 'Cilan / Chili / Cress', 'badge': 'Trío', 'type': 'Planta'},
            {'region': 'Teselia / Unova', 'town': 'Ciudad Esmaltada', 'leader': 'Lenora', 'badge': 'Base', 'type': 'Normal'},
            {'region': 'Teselia / Unova', 'town': 'Ciudad Porcelana', 'leader': 'Burgh', 'badge': 'Elitro', 'type': 'Bicho'},
            {'region': 'Teselia / Unova', 'town': 'Ciudad Mayólica', 'leader': 'Elesa', 'badge': 'Voltio', 'type': 'Eléctrico'},
            {'region': 'Teselia / Unova', 'town': 'Ciudad Fayenza', 'leader': 'Clay', 'badge': 'Sismo', 'type': 'Tierra'},
            {'region': 'Teselia / Unova', 'town': 'Ciudad Loza', 'leader': 'Skyla', 'badge': 'Jet', 'type': 'Volador'},
            {'region': 'Teselia / Unova', 'town': 'Ciudad Cirrus', 'leader': 'Brycen', 'badge': 'Helada', 'type': 'Hielo'},
            {'region': 'Teselia / Unova', 'town': 'Ciudad Caolín', 'leader': 'Drayden', 'badge': 'Leyenda', 'type': 'Dragón'},

            # Gen 6 - Kalos
            {'region': 'Kalos', 'town': 'Ciudad Novarte', 'leader': 'Viola', 'badge': 'Insecto', 'type': 'Bicho'},
            {'region': 'Kalos', 'town': 'Ciudad Relieve', 'leader': 'Grant', 'badge': 'Muro', 'type': 'Roca'},
            {'region': 'Kalos', 'town': 'Ciudad Yantra', 'leader': 'Korrina', 'badge': 'Lidia', 'type': 'Lucha'},
            {'region': 'Kalos', 'town': 'Ciudad Témpera', 'leader': 'Ramos', 'badge': 'Hoja', 'type': 'Planta'},
            {'region': 'Kalos', 'town': 'Ciudad Luminalia', 'leader': 'Clemont', 'badge': 'Voltaje', 'type': 'Eléctrico'},
            {'region': 'Kalos', 'town': 'Ciudad Romantis', 'leader': 'Valerie', 'badge': 'Hada', 'type': 'Hada'},
            {'region': 'Kalos', 'town': 'Ciudad Fluxus', 'leader': 'Olympia', 'badge': 'Psique', 'type': 'Psíquico'},
            {'region': 'Kalos', 'town': 'Ciudad Fractal', 'leader': 'Wulfric', 'badge': 'Iceberg', 'type': 'Hielo'},

            # Gen 7 - Alola
            # Alola utiliza pruebas y no gimnasios tradicionales.
            # Se omiten los gimnasios de esta región.

            # Gen 8 - Galar
            {'region': 'Galar', 'town': 'Ciudad Pistón', 'leader': 'Milo', 'badge': 'Planta', 'type': 'Planta'},
            {'region': 'Galar', 'town': 'Pueblo Hoyuelo', 'leader': 'Nessa', 'badge': 'Agua', 'type': 'Agua'},
            {'region': 'Galar', 'town': 'Ciudad Artejo', 'leader': 'Kabu', 'badge': 'Fuego', 'type': 'Fuego'},
            {'region': 'Galar', 'town': 'Pueblo Ladera', 'leader': 'Bea / Allister', 'badge': 'Lucha / Fantasma', 'type': 'Lucha'},
            {'region': 'Galar', 'town': 'Pueblo Crampón', 'leader': 'Marnie / Piers', 'badge': 'Siniestro', 'type': 'Siniestro'},
            {'region': 'Galar', 'town': 'Pueblo Auriga', 'leader': 'Gordie / Melony', 'badge': 'Roca / Hielo', 'type': 'Roca'},
            {'region': 'Galar', 'town': 'Ciudad Puntera', 'leader': 'Raihan', 'badge': 'Dragón', 'type': 'Dragón'},

            # Gen 9 - Paldea
            {'region': 'Paldea', 'town': 'Pueblo Cerezal', 'leader': 'Katy', 'badge': 'Bicho', 'type': 'Bicho'},
            {'region': 'Paldea', 'town': 'Ciudad Meseta', 'leader': 'Brassius', 'badge': 'Planta', 'type': 'Planta'},
            {'region': 'Paldea', 'town': 'Ciudad Leudal', 'leader': 'Iono', 'badge': 'Eléctrico', 'type': 'Eléctrico'},
            {'region': 'Paldea', 'town': 'Ciudad Mestura', 'leader': 'Larry', 'badge': 'Normal', 'type': 'Normal'},
            {'region': 'Paldea', 'town': 'Pueblo Hozkailu', 'leader': 'Ryme', 'badge': 'Fantasma', 'type': 'Fantasma'},
            {'region': 'Paldea', 'town': 'Ciudad Alfornada', 'leader': 'Tulip', 'badge': 'Psíquico', 'type': 'Psíquico'},
            {'region': 'Paldea', 'town': 'Sierra Napada', 'leader': 'Grusha', 'badge': 'Hielo', 'type': 'Hielo'},
        ]

        # Registrar los gimnasios
        for g in gyms_data:
            type_obj, _ = Type.objects.get_or_create(name=g['type'])
            region_obj = Region.objects.get(name=g['region'])

            Gym.objects.update_or_create(
                town=g['town'],
                region=region_obj,
                defaults={
                    'leader_name': g['leader'],
                    'badge_name': g['badge'],
                    'element_type': type_obj
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "¡Regiones y gimnasios cargados correctamente sin imágenes de medallas!"
            )
        )
