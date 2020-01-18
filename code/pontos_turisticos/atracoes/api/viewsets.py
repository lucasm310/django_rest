from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from atracoes.models import Atracoes
from .serializers import AtracoesGeralSerializer

class AtracoesViewSet(ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]

	queryset = Atracoes.objects.all()
	serializer_class = AtracoesGeralSerializer
	
	filter_backends = [filters.SearchFilter]
	search_fields = ['nome']
