from django.db import models

def uploadImage(instance, filename):
    return f'funcs/{instance.nome}/{filename}'


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    salario = models.CharField(max_length=10)
    foto = models.ImageField(upload_to=uploadImage, blank=True, null=True)

    def __str__(self):
        return self.nome