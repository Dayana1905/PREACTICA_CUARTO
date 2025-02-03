from django.db import models

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField()  # Campo correo, obligatorio por defecto

    def __str__(self):
        return self.nombre
