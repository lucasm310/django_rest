from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesResSerializer
from comentarios.api.serializers import ComentariosResSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer
from users.api.serializers import UserListSerializer


class PontoTuristicoSerializer(ModelSerializer):
	atracoes = AtracoesResSerializer(many=True, read_only=True, required=False)
	comentarios = ComentariosResSerializer(many=True, read_only=True, required=False)
	avaliacoes = AvaliacoesSerializer(many=True, read_only=True, required=False)
	cadastrado_por = UserListSerializer(read_only=True)

	class Meta:
		model = PontoTuristico
		fields = ['id','nome', 'descricao','linha1','linha2','cidade',
				'estado','pais','atracoes','comentarios','avaliacoes','cadastrado_por']
		extra_kwargs = {'cadastrado_por': {'read_only':True}}