from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from comentarios.models import Comentarios
from .serializers import ComentariosSerializer

class ComentariosViewSet(ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	queryset = Comentarios.objects.all()
	serializer_class = ComentariosSerializer


	def perform_create(self, serializer):
		serializer.save(usuario=self.request.user)
