from rest_framework import serializers
from api_telemetria import models

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = "__all__"

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = "__all__"

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = "__all__"

class MedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicao
        fields = "__all__"

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = "__all__"

class MedicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicaoVeiculo
        fields = "__all__"
        extra_kwargs = {
            'id':{'help_text':'identificador de Medição veiculo'},
            'veiculoid':{'help_text':'identificador do veiculo. Buscar no get da Api veiculo' },
            'medicaoid': {'help_text': 'identificador do tipo de medição. Buscar no Get da api medição'},
            'data': {'help_text': 'data e hora da medição realizada, essa informação deve vir da automação'},
            'valor': {'help_text': 'valor medido na automação.'}
        }