
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name.capitalize()


class Ability(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name.capitalize()


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)
    generation = models.IntegerField(
        help_text="Generación (1 al 9)"
    )
    professor = models.CharField(
        max_length=100,
        help_text="Nombre del Profesor"
    )

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    CATEGORY_CHOICES = [
        ('normal', 'Normal'),
        ('legendary', 'Legendario'),
        ('mythical', 'Singular'),
    ]

    poke_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    spanish_name = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )
    height = models.FloatField(
        help_text="Altura en metros"
    )
    weight = models.FloatField(
        help_text="Peso en kg"
    )
    sprite_url = models.URLField(
        max_length=500,
        help_text="Imagen del Pokémon"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='normal'
    )

    # Estadísticas base
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    special_attack = models.IntegerField(default=0)
    special_defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    # Relaciones
    evolves_from = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='evolutions'
    )

    types = models.ManyToManyField(
        Type,
        related_name="pokemons"
    )

    abilities = models.ManyToManyField(
        Ability,
        related_name="pokemons"
    )

    def __str__(self):
        display_name = (
            self.spanish_name
            if self.spanish_name
            else self.name.capitalize()
        )
        return f"#{self.poke_id} {display_name}"


class Gym(models.Model):
    leader_name = models.CharField(max_length=100)

    element_type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="gyms"
    )

    badge_name = models.CharField(max_length=100)

    town = models.CharField(max_length=100)

    phone = models.CharField(
        max_length=20,
        blank=True,
        default=''
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="gyms"
    )

    def __str__(self):
        return (
            f"Gimnasio {self.town} ({self.region.name}) "
            f"- Líder {self.leader_name}"
        )


class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_id = models.CharField(
        max_length=20,
        unique=True
    )
    hometown = models.CharField(max_length=100)
    assigned_professor = models.CharField(max_length=100)
    leagues_participated = models.TextField()
    qualified_for_league = models.BooleanField(default=False)

    team = models.ManyToManyField(
        Pokemon,
        blank=True,
        related_name="trainers_in_team"
    )

    # Medallas ganadas por el entrenador
    badges = models.ManyToManyField(
        Gym,
        blank=True,
        related_name="trainers_with_badge"
    )

    @property
    def pokemon_count(self):
        return self.team.count()

    @property
    def badge_count(self):
        return self.badges.count()

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} "
            f"({self.document_id})"
        )


class Backup(models.Model):
    trainer = models.OneToOneField(
        Trainer,
        on_delete=models.CASCADE,
        related_name="backup"
    )

    caretaker_professor = models.CharField(max_length=100)

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="backups"
    )

    items = models.TextField(blank=True)

    stored_pokemons = models.ManyToManyField(
        Pokemon,
        blank=True,
        related_name="backups_stored"
    )

    @property
    def pokemon_count(self):
        return self.stored_pokemons.count()

    def __str__(self):
        return (
            f"Backup/PC de {self.trainer.first_name} "
            f"({self.region.name})"
        )
