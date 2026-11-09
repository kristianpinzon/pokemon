from django.core.management.base import BaseCommand
from pokedex.models import Gym, Type

class Command(BaseCommand):
    help = 'Carga los Gimnasios oficiales de todas las regiones en PostgreSQL'

    def handle(self, *args, **options):
        gyms = [
            # --- KANTO ---
            ("Brock", "Roca", "Medalla Roca", "Ciudad Plateada", "+34 91 101 0001", "Kanto"),
            ("Misty", "Agua", "Medalla Cascada", "Ciudad Celeste", "+34 91 101 0002", "Kanto"),
            ("Teniente Surge", "Eléctrico", "Medalla Trueno", "Ciudad Carmín", "+34 91 101 0003", "Kanto"),
            ("Erika", "Planta", "Medalla Arcoíris", "Ciudad Azulona", "+34 91 101 0004", "Kanto"),
            ("Koga", "Veneno", "Medalla Alma", "Ciudad Fucsia", "+34 91 101 0005", "Kanto"),
            ("Sabrina", "Psíquico", "Medalla Pantano", "Ciudad Azafrán", "+34 91 101 0006", "Kanto"),
            ("Blaine", "Fuego", "Medalla Volcán", "Isla Canela", "+34 91 101 0007", "Kanto"),
            ("Giovanni", "Tierra", "Medalla Tierra", "Ciudad Verde", "+34 91 101 0008", "Kanto"),

            # --- JOHTO ---
            ("Pegaso", "Volador", "Medalla Céfiro", "Ciudad Malva", "+81 75 202 0001", "Johto"),
            ("Antón", "Bicho", "Medalla Colmena", "Pueblo Azalea", "+81 75 202 0002", "Johto"),
            ("Blanca", "Normal", "Medalla Planicie", "Ciudad Trigal", "+81 75 202 0003", "Johto"),
            ("Morti", "Fantasma", "Medalla Niebla", "Ciudad Iris", "+81 75 202 0004", "Johto"),
            ("Aníbal", "Lucha", "Medalla Tormenta", "Ciudad Orquídea", "+81 75 202 0005", "Johto"),
            ("Yasmina", "Acero", "Medalla Mineral", "Ciudad Olivo", "+81 75 202 0006", "Johto"),
            ("Fredo", "Hielo", "Medalla Glaciar", "Pueblo Caoba", "+81 75 202 0007", "Johto"),
            ("Débora", "Dragón", "Medalla Dragón", "Ciudad Endrino", "+81 75 202 0008", "Johto"),

            # --- HOENN ---
            ("Petra", "Roca", "Medalla Piedra", "Ciudad Férrica", "+1 305 303 0001", "Hoenn"),
            ("Marcial", "Lucha", "Medalla Puño", "Pueblo Azuliza", "+1 305 303 0002", "Hoenn"),
            ("Erico", "Eléctrico", "Medalla Dinamo", "Ciudad Malvalona", "+1 305 303 0003", "Hoenn"),
            ("Candela", "Fuego", "Medalla Calor", "Pueblo Lavacalda", "+1 305 303 0004", "Hoenn"),
            ("Norman", "Normal", "Medalla Equilibrio", "Ciudad Petalia", "+1 305 303 0005", "Hoenn"),
            ("Alana", "Volador", "Medalla Pluma", "Ciudad Arborada", "+1 305 303 0006", "Hoenn"),
            ("Vito y Leti", "Psíquico", "Medalla Mente", "Ciudad Algaria", "+1 305 303 0007", "Hoenn"),
            ("Galano", "Agua", "Medalla Lluvia", "Arrecípolis", "+1 305 303 0008", "Hoenn"),

            # --- SINNOH ---
            ("Roco", "Roca", "Medalla Carbón", "Ciudad Pirita", "+81 11 404 0001", "Sinnoh"),
            ("Gardenia", "Planta", "Medalla Bosque", "Ciudad Vetusta", "+81 11 404 0002", "Sinnoh"),
            ("Brezo", "Lucha", "Medalla Adoquín", "Ciudad Rocavelo", "+81 11 404 0003", "Sinnoh"),
            ("Mananti", "Agua", "Medalla Ciénaga", "Ciudad Pradera", "+81 11 404 0004", "Sinnoh"),
            ("Fantina", "Fantasma", "Medalla Reliquia", "Ciudad Corazón", "+81 11 404 0005", "Sinnoh"),
            ("Acerón", "Acero", "Medalla Mina", "Ciudad Canal", "+81 11 404 0006", "Sinnoh"),
            ("Inverna", "Hielo", "Medalla Carámbano", "Ciudad Puntaneva", "+81 11 404 0007", "Sinnoh"),
            ("Lectro", "Eléctrico", "Medalla Faro", "Ciudad Marina", "+81 11 404 0008", "Sinnoh"),

            # --- TESELIA / UNOVA ---
            ("Cilantro, Maíz y Koga", "Planta", "Medalla Trío", "Ciudad Gres", "+1 212 505 0001", "Teselia"),
            ("Aloe", "Normal", "Medalla Base", "Ciudad Esmaltada", "+1 212 505 0002", "Teselia"),
            ("Camus", "Bicho", "Medalla Élitro", "Ciudad Porcelana", "+1 212 505 0003", "Teselia"),
            ("Camila", "Eléctrico", "Medalla Voltio", "Ciudad Mayólica", "+1 212 505 0004", "Teselia"),
            ("Yakón", "Tierra", "Medalla Temblor", "Ciudad Fayenza", "+1 212 505 0005", "Teselia"),
            ("Gerania", "Volador", "Medalla Pluma", "Ciudad Loza", "+1 212 505 0006", "Teselia"),
            ("Junco", "Hielo", "Medalla Cárambano", "Ciudad Teca", "+1 212 505 0007", "Teselia"),
            ("Lirio", "Dragón", "Medalla Leyenda", "Ciudad Caolín", "+1 212 505 0008", "Teselia"),

            # --- KALOS ---
            ("Violeta", "Bicho", "Medalla Insecto", "Ciudad Novarte", "+33 1 606 0001", "Kalos"),
            ("Lino", "Roca", "Medalla Muro", "Ciudad Relieve", "+33 1 606 0002", "Kalos"),
            ("Corelia", "Lucha", "Medalla Lid", "Ciudad Yantar", "+33 1 606 0003", "Kalos"),
            ("Amaro", "Planta", "Medalla Hoja", "Ciudad Témpera", "+33 1 606 0004", "Kalos"),
            ("Clemont / Lem", "Eléctrico", "Medalla Voltaje", "Ciudad Luminalia", "+33 1 606 0005", "Kalos"),
            ("Valeria", "Hada", "Medalla Hada", "Ciudad Romantis", "+33 1 606 0006", "Kalos"),
            ("Astrid", "Psíquico", "Medalla Psique", "Ciudad Anistar", "+33 1 606 0007", "Kalos"),
            ("É сним / Édel", "Hielo", "Medalla Iceberg", "Ciudad Fractal", "+33 1 606 0008", "Kalos"),

            # --- GALAR ---
            ("Paco", "Planta", "Medalla Planta", "Pueblo Hoyuelo", "+44 20 707 0001", "Galar"),
            ("Cati", "Agua", "Medalla Agua", "Pueblo Amura", "+44 20 707 0002", "Galar"),
            ("Naboru", "Fuego", "Medalla Fuego", "Ciudad Motorstoke", "+44 20 707 0003", "Galar"),
            ("Judith", "Lucha", "Medalla Lucha", "Pueblo Ladera", "+44 20 707 0004", "Galar"),
            ("Valeria / Sally", "Hada", "Medalla Hada", "Pueblo Puntera", "+44 20 707 0005", "Galar"),
            ("Gordie", "Roca", "Medalla Roca", "Pueblo Auriga", "+44 20 707 0006", "Galar"),
            ("Nerio", "Siniestro", "Medalla Siniestra", "Pueblo Spikford", "+44 20 707 0007", "Galar"),
            ("Roy", "Dragón", "Medalla Dragón", "Ciudad Artejo", "+44 20 707 0008", "Galar"),

            # --- PALDEA ---
            ("Aracelio", "Bicho", "Medalla Bicho", "Pueblo Cortondo", "+34 96 808 0001", "Paldea"),
            ("Brazo", "Planta", "Medalla Planta", "Pueblo Altamía", "+34 96 808 0002", "Paldea"),
            ("e-Nigma", "Eléctrico", "Medalla Eléctrica", "Ciudad Leudaldia", "+34 96 808 0003", "Paldea"),
            ("Kofu", "Agua", "Medalla Agua", "Ciudad Cántara", "+34 96 808 0004", "Paldea"),
            ("Laureano", "Normal", "Medalla Normal", "Pueblo Medali", "+34 96 808 0005", "Paldea"),
            ("Lima", "Fantasma", "Medalla Fantasma", "Pueblo Hozgarrada", "+34 96 808 0006", "Paldea"),
            ("Tuli", "Psíquico", "Medalla Psíquica", "Pueblo Alfornía", "+34 96 808 0007", "Paldea"),
            ("Grusha", "Hielo", "Medalla Hielo", "Sierra Napada", "+34 96 808 0008", "Paldea"),
        ]

        self.stdout.write("Cargando Gimnasios oficiales de todas las regiones...")

        for leader, type_name, badge, town, phone, region in gyms:
            t_obj, _ = Type.objects.get_or_create(name=type_name)
            Gym.objects.update_or_create(
                town=town,
                region=region,
                defaults={
                    'leader_name': leader,
                    'element_type': t_obj,
                    'badge_name': badge,
                    'phone': phone,
                }
            )

        self.stdout.write(self.style.SUCCESS("¡Todos los Gimnasios de Kanto a Paldea han sido pre-cargados con éxito!"))