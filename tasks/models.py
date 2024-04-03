from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=35)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField()
    time = models.TimeField()
    completa = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f'{self.titulo}'
