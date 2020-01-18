from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from avaliacoes.models import Avaliacoes
from .serializers import AvaliacoesSerializer

class AvaliacoesViewSet(ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]
	
	queryset = Avaliacoes.objects.all()
	serializer_class = AvaliacoesSerializer

	def perform_create(self, serializer):
		serializer.save(usuario=self.request.user)
