from django.db import models

class Produto(models.Model):
    MARCAS_CHOICES = [
        ('livealoe', 'Livealoe'),
        ('laszlo', 'Laszlo'),
        ('terra_flor', 'Terra Flor'),
        ('amo_karite', 'Amo Karitê'),
    ]

    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, choices=MARCAS_CHOICES)
    descricao_curta = models.TextField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/') # Salva em media/produtos/

    def __str__(self):
        return self.nome
    @property
    def valor_parcela(self):
        if self.preco:
            return self.preco / 3
        return 0