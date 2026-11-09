from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Pokemon, Trainer, Gym, Type
from .forms import TrainerForm, GymForm

# --- DASHBOARD / VISTA PRINCIPAL ---
def index(request):
    section = request.GET.get('section', 'trainers')
    query = request.GET.get('q', '').strip()

    trainers = Trainer.objects.all()
    pokemons = Pokemon.objects.all().order_by('poke_id')
    gyms = Gym.objects.select_related('element_type').all()

    if query:
        if section == 'trainers':
            trainers = trainers.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(document_id__icontains=query) |
                Q(hometown__icontains=query)
            )
        elif section == 'pokemons':
            pokemons = pokemons.filter(
                Q(name__icontains=query) |
                Q(spanish_name__icontains=query) |
                Q(poke_id__icontains=query)
            )
        elif section == 'gyms':
            gyms = gyms.filter(
                Q(leader_name__icontains=query) |
                Q(town__icontains=query) |
                Q(badge_name__icontains=query) |
                Q(region__icontains=query) |
                Q(element_type__name__icontains=query)
            )

    context = {
        'section': section,
        'query': query,
        'trainers': trainers,
        'pokemons': pokemons,
        'gyms': gyms,
    }
    return render(request, 'pokedex/index.html', context)


# --- DETALLE DE POKÉMON ---
def pokemon_detail(request, poke_id):
    pokemon = get_object_or_404(Pokemon, poke_id=poke_id)

    prev_pokemon = None
    next_pokemon = None

    if pokemon.category == 'normal':
        if hasattr(pokemon, 'previous_evolution') and pokemon.previous_evolution:
            prev_pokemon = pokemon.previous_evolution
        elif hasattr(pokemon, 'evolves_from') and pokemon.evolves_from:
            prev_pokemon = pokemon.evolves_from

        if hasattr(pokemon, 'next_evolution') and pokemon.next_evolution:
            next_pokemon = pokemon.next_evolution
        else:
            if hasattr(Pokemon, 'previous_evolution'):
                next_pokemon = Pokemon.objects.filter(previous_evolution=pokemon).first()
            elif hasattr(Pokemon, 'evolves_from'):
                next_pokemon = Pokemon.objects.filter(evolves_from=pokemon).first()

    context = {
        'pokemon': pokemon,
        'prev_pokemon': prev_pokemon,
        'next_pokemon': next_pokemon,
    }
    return render(request, 'pokedex/detail.html', context)


# --- DETALLE DE ENTRENADOR ---
def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer.objects.prefetch_related('team', 'badges'), id=trainer_id)
    return render(request, 'pokedex/trainer_detail.html', {'trainer': trainer})


# --- CRUD ENTRENADORES ---
def trainer_create(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Entrenador registrado con éxito!')
            return redirect('/?section=trainers')
        else:
            messages.error(request, 'Error al guardar el formulario. Por favor revisa los datos ingresados.')
    else:
        form = TrainerForm()

    return render(request, 'pokedex/editar_crear.html', {
        'form': form,
        'title': 'Registrar Nuevo Entrenador'
    })

def trainer_edit(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Información del entrenador actualizada!')
            return redirect('/?section=trainers')
        else:
            messages.error(request, 'Error al actualizar. Revisa los campos resaltados.')
    else:
        form = TrainerForm(instance=trainer)

    return render(request, 'pokedex/editar_crear.html', {
        'form': form,
        'title': f'Editar Entrenador: {trainer.first_name} {trainer.last_name}'
    })

def trainer_delete(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        trainer.delete()
        messages.success(request, 'Entrenador eliminado correctamente.')
        return redirect('/?section=trainers')

    return render(request, 'pokedex/confirm_delete.html', {
        'object': f'{trainer.first_name} {trainer.last_name}',
        'cancel_url': '/?section=trainers'
    })


# --- CRUD GIMNASIOS ---
def gym_create(request):
    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gimnasio creado con éxito!')
            return redirect('/?section=gyms')
        else:
            messages.error(request, 'Error al crear el gimnasio. Revisa los campos.')
    else:
        form = GymForm()

    return render(request, 'pokedex/editar_crear.html', {
        'form': form,
        'title': 'Crear Nuevo Gimnasio'
    })

def gym_edit(request, gym_id):
    gym = get_object_or_404(Gym, id=gym_id)
    if request.method == 'POST':
        form = GymForm(request.POST, instance=gym)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gimnasio actualizado correctamente!')
            return redirect('/?section=gyms')
        else:
            messages.error(request, 'Error al actualizar el gimnasio.')
    else:
        form = GymForm(instance=gym)

    return render(request, 'pokedex/editar_crear.html', {
        'form': form,
        'title': f'Editar Gimnasio de {gym.town}'
    })

def gym_delete(request, gym_id):
    gym = get_object_or_404(Gym, id=gym_id)
    if request.method == 'POST':
        gym.delete()
        messages.success(request, 'Gimnasio eliminado correctamente.')
        return redirect('/?section=gyms')

    return render(request, 'pokedex/confirm_delete.html', {
        'object': f'Gimnasio de {gym.town} ({gym.leader_name})',
        'cancel_url': '/?section=gyms'
    })