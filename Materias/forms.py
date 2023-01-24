from django import forms
from django.forms import ModelForm
from .models import Materias


class CrearMateriasForm(ModelForm):
    class Meta:
        model = Materias
        fields = ['titulo', 'descripcion', 'correlativa']