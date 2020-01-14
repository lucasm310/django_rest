from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from atracoes.models import Atracoes
from .serializers import AtracoesGeralSerializer

class AtracoesViewSet(ModelViewSet):
	queryset = Atracoes.objects.all()
	serializer_class = AtracoesGeralSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['nome']
