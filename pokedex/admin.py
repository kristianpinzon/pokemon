from django.contrib import admin
from .models import Type, Ability, Region, Pokemon, Gym, Trainer, Backup

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'generation', 'professor')
    list_filter = ('generation',)
    search_fields = ('name', 'professor')


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('poke_id', 'spanish_name', 'name', 'category', 'height', 'weight')
    list_filter = ('category', 'types')
    search_fields = ('name', 'spanish_name', 'poke_id')


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('id', 'town', 'region', 'leader_name', 'badge_name', 'element_type')
    list_filter = ('region', 'element_type')
    search_fields = ('town', 'leader_name', 'badge_name')


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'document_id', 'hometown', 'qualified_for_league')
    list_filter = ('qualified_for_league',)
    search_fields = ('first_name', 'last_name', 'document_id')
    filter_horizontal = ('team', 'badges')


@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    list_display = ('id', 'trainer', 'caretaker_professor', 'region')
    list_filter = ('region',)
    search_fields = ('trainer__first_name', 'trainer__last_name', 'caretaker_professor')
    filter_horizontal = ('stored_pokemons',)