from django.db import models

class Contact(models.Model):
    Nombre = models.CharField(max_length=50)
    Email = models.EmailField()
    Celular = models.CharField(max_length=10)
    Mensaje = models.TextField()

    def __str__(self):
        return self.name
