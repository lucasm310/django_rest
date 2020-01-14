from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracoes

class AtracoesGeralSerializer(ModelSerializer):
	class Meta:
		model = Atracoes
		fields = ['id','ponto_turistico','nome','descricao','horario_func','idade_minima']

class AtracoesResSerializer(ModelSerializer):
	class Meta:
		model = Atracoes
		fields = ['id','nome']