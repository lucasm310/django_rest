from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacoes
from users.api.serializers import UserListSerializer


class AvaliacoesSerializer(ModelSerializer):
	usuario = UserListSerializer(read_only=True)
	class Meta:
		model = Avaliacoes
		fields = ['id','usuario','comentario','nota','data','ponto_turistico']
		extra_kwargs = {'usuario': {'read_only':True}}