from django.urls import path
from . import views

urlpatterns = [
    # Principal
    path('', views.index, name='index'),

    # Detalles
    path('pokemon/<int:poke_id>/', views.pokemon_detail, name='pokemon_detail'),
    path('trainer/<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),

    # CRUD Entrenadores
    path('trainer/new/', views.trainer_create, name='trainer_create'),
    path('trainer/<int:trainer_id>/edit/', views.trainer_edit, name='trainer_edit'),
    path('trainer/<int:trainer_id>/delete/', views.trainer_delete, name='trainer_delete'),

    # CRUD Gimnasios
    path('gym/new/', views.gym_create, name='gym_create'),
    path('gym/<int:gym_id>/edit/', views.gym_edit, name='gym_edit'),
    path('gym/<int:gym_id>/delete/', views.gym_delete, name='gym_delete'),
]