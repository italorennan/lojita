from django.db import models
from produtos.models import Produto
from django.contrib.auth.models import User

# Create your models here.
MOVIMENTO=(
    ('e','entrada'),
    ('s','saída'),
)

class TimeStampedModel(models.Model):
    created=models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified=models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )
    class Meta:
        abstract=True


class Estoque(TimeStampedModel):
    funcionario=models.ForeignKey(User,on_delete=models.CASCADE)
    notafiscal=models.PositiveIntegerField('nota fiscal',null=True,blank=True)
    movimento=models.CharField(max_length=1,choices=MOVIMENTO)
    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return str(self.pk)

class EstoqueItens(models.Model):
    estoque=models.ForeignKey(Estoque,on_delete=models.CASCADE,related_name='estoques')
    produto=models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade=models.PositiveIntegerField()
    saldo=models.PositiveIntegerField()
    
    class Meta:
        ordering=('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk,self.estoque.pk,self.produto)