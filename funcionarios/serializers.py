from rest_framework import serializers
from .models import Funcionario

class FuncionariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = '__all__'