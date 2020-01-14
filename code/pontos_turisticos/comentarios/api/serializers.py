from rest_framework.serializers import ModelSerializer, SlugRelatedField
from comentarios.models import Comentarios
from users.api.serializers import UserListSerializer

class ComentariosSerializer(ModelSerializer):
	usuario = UserListSerializer(read_only=True)
	class Meta:
		model = Comentarios
		fields = ['id','usuario','comentario','data','aprovado','ponto_turistico']
		extra_kwargs = {"usuario": {"read_only": True}}

class ComentariosResSerializer(ModelSerializer):
	usuario = UserListSerializer(read_only=True)

	class Meta:
		model = Comentarios
		fields = ['id', 'usuario','comentario','data']
