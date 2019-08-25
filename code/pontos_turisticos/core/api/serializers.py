from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer
from enderecos.api.serializers import EnderecosSerializer
from comentarios.api.serializers import ComentariosSerializer

class PontoTuristicoSerializer(ModelSerializer):
	atracoes = AtracoesSerializer(many=True)
	avaliacoes = AvaliacoesSerializer(many=True)
	enderecos = EnderecosSerializer()
	comentarios = ComentariosSerializer(many=True)

	class Meta:
		model = PontoTuristico
		fields = ['nome', 'descricao', 'atracoes',
		'comentarios', 'avaliacoes', 'enderecos']