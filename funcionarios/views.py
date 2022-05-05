from rest_framework import viewsets
from .models import Funcionario
from .serializers import FuncionariosSerializer

class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionariosSerializer