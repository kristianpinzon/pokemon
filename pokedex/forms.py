from django import forms
from .models import Pokemon, Trainer, Gym, Type

# --- OPCIONES OFICIALES Y EN ESPAÑOL ---

REGIONS_CHOICES = [
    ('Kanto', 'Kanto'),
    ('Johto', 'Johto'),
    ('Hoenn', 'Hoenn'),
    ('Sinnoh', 'Sinnoh'),
    ('Teselia', 'Teselia'),
    ('Kalos', 'Kalos'),
    ('Alola', 'Alola'),
    ('Galar', 'Galar'),
    ('Paldea', 'Paldea'),
]

LEADERS_CHOICES = [
    ('Brock', 'Brock (Ciudad Plateada - Kanto)'),
    ('Misty', 'Misty (Ciudad Celeste - Kanto)'),
    ('Teniente Surge', 'Teniente Surge (Ciudad Carmín - Kanto)'),
    ('Erika', 'Erika (Ciudad Azulona - Kanto)'),
    ('Koga', 'Koga (Ciudad Fucsia - Kanto)'),
    ('Sabrina', 'Sabrina (Ciudad Azafrán - Kanto)'),
    ('Blaine', 'Blaine (Isla Canela - Kanto)'),
    ('Giovanni', 'Giovanni (Ciudad Verde - Kanto)'),
]

BADGES_CHOICES = [
    ('Medalla Roca', 'Medalla Roca'),
    ('Medalla Cascada', 'Medalla Cascada'),
    ('Medalla Trueno', 'Medalla Trueno'),
    ('Medalla Arcoíris', 'Medalla Arcoíris'),
    ('Medalla Alma', 'Medalla Alma'),
    ('Medalla Pantano', 'Medalla Pantano'),
    ('Medalla Volcán', 'Medalla Volcán'),
    ('Medalla Tierra', 'Medalla Tierra'),
]

TOWNS_CHOICES = [
    ('Ciudad Plateada', 'Ciudad Plateada'),
    ('Ciudad Celeste', 'Ciudad Celeste'),
    ('Ciudad Carmín', 'Ciudad Carmín'),
    ('Ciudad Azulona', 'Ciudad Azulona'),
    ('Isla Canela', 'Isla Canela'),
    ('Ciudad Verde', 'Ciudad Verde'),
]

PROFESSORS_BY_REGION = [
    ('Profesor Oak (Kanto)', 'Profesor Oak (Kanto)'),
    ('Profesor Elm (Johto)', 'Profesor Elm (Johto)'),
    ('Profesor Abedul (Hoenn)', 'Profesor Abedul (Hoenn)'),
    ('Profesor Serbal (Sinnoh)', 'Profesor Serbal (Sinnoh)'),
    ('Profesora Encina (Teselia)', 'Profesora Encina (Teselia)'),
    ('Profesor Ciprés (Kalos)', 'Profesor Ciprés (Kalos)'),
    ('Profesor Kukui (Alola)', 'Profesor Kukui (Alola)'),
    ('Profesora Magnolia (Galar)', 'Profesora Magnolia (Galar)'),
    ('Profesora Sada / Profesor Turo (Paldea)', 'Profesora Sada / Profesor Turo (Paldea)'),
]

REGION_LEAGUES = [
    ('Liga Kanto (Añil)', 'Liga Kanto (Añil)'),
    ('Liga Johto (Plateada)', 'Liga Johto (Plateada)'),
    ('Liga Hoenn (Siempre Grande)', 'Liga Hoenn (Siempre Grande)'),
    ('Liga Sinnoh (Lirio del Valle)', 'Liga Sinnoh (Lirio del Valle)'),
    ('Liga Teselia (Vertress)', 'Liga Teselia (Vertress)'),
    ('Liga Kalos (Lumiose)', 'Liga Kalos (Lumiose)'),
    ('Liga Alola (Manalo)', 'Liga Alola (Manalo)'),
    ('Liga Galar (Wyndon)', 'Liga Galar (Wyndon)'),
    ('Liga Paldea', 'Liga Paldea'),
]


# --- FORMULARIO DE GIMNASIO ---
class GymForm(forms.ModelForm):
    element_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Tipo Elemental del Gimnasio",
        empty_label="- Selecciona un tipo elemental -"
    )
    leader_name = forms.ChoiceField(
        choices=LEADERS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Líder de Gimnasio"
    )
    badge_name = forms.ChoiceField(
        choices=BADGES_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Nombre de la Medalla"
    )
    town = forms.ChoiceField(
        choices=TOWNS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Ciudad o Pueblo"
    )
    region = forms.ChoiceField(
        choices=REGIONS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Región"
    )

    class Meta:
        model = Gym
        fields = ['leader_name', 'element_type', 'badge_name', 'town', 'phone', 'region']
        labels = {
            'leader_name': 'Líder de Gimnasio',
            'element_type': 'Tipo Elemental del Gimnasio',
            'badge_name': 'Medalla',
            'town': 'Ciudad o Pueblo',
            'phone': 'Teléfono de Contacto',
            'region': 'Región',
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. +57 300 1234567'}),
        }


# --- FORMULARIO DE ENTRENADOR ---
class TrainerForm(forms.ModelForm):
    assigned_professor = forms.ChoiceField(
        choices=PROFESSORS_BY_REGION,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Profesor Asignado"
    )

    leagues_participated = forms.MultipleChoiceField(
        choices=REGION_LEAGUES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
        label="Ligas en las que ha participado",
        required=False
    )

    badges = forms.ModelMultipleChoiceField(
        queryset=Gym.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
        label="Medallas de Gimnasio Obtenidas",
        required=False
    )

    class Meta:
        model = Trainer
        fields = [
            'first_name', 'last_name', 'document_id', 'hometown',
            'assigned_professor', 'leagues_participated', 'qualified_for_league',
            'team', 'badges'
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'document_id': 'Documento de Identidad',
            'hometown': 'Pueblo o Ciudad de Origen',
            'assigned_professor': 'Profesor Asignado',
            'qualified_for_league': '¿Clasificado a la Liga Actual?',
            'team': 'Equipo Activo (Máximo 6 Pokémon)',
            'badges': 'Medallas de Gimnasio Obtenidas',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Ash'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Ketchum'}),
            'document_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1098765432'}),
            'hometown': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pueblo Paleta'}),
            'qualified_for_league': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'team': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
        }

    def clean_leagues_participated(self):
        leagues = self.cleaned_data.get('leagues_participated')
        if isinstance(leagues, list):
            return ", ".join(leagues)
        return leagues or ""

    def clean_team(self):
        team = self.cleaned_data.get('team')
        if team and team.count() > 6:
            raise forms.ValidationError("Un entrenador no puede llevar más de 6 Pokémon en su equipo activo.")
        return team