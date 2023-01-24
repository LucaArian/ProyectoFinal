from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Materias(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    fechacreada = models.DateTimeField(auto_now_add=True)
    fecharendida = models.DateTimeField(null=True, blank=True)
    correlativa = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo 