from django.db import models

# Create your models here.
class Produto(models.Model):
    nome=models.CharField(max_length=100)
    preco=models.DecimalField(max_digits=7,decimal_places=2)
    estoque=models.IntegerField('estoque atual')
    descricao=models.TextField()
    class Meta:
        ordering=('nome',)

    def __str__(self):
        return self.nome
    
    def to_dict_json(self):
            return {
            'pk': self.pk,
            'produto': self.nome,
            'estoque': self.estoque,
        }
