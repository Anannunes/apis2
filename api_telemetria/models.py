from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Medicao(models.Model):
    tipo = models.CharField(max_length=25)
    unidadeMedidaId = models.ForeignKey(UnidadeMedida, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tipo

class Veiculo(models.Model):
    descricao = models.CharField(max_length=100)
    marcaId = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    modeloId = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING)
    ano = models.IntegerField(max_length=4)
    horimetro = models.IntegerField(max_length=4)
    
    def __str__(self):
        return self.descricao
    
class MedicaoVeiculo(models.Model):
    veiculoId = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)
    medicaoId = models.ForeignKey(Medicao, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.valor