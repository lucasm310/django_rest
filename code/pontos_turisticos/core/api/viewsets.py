from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework import filters

class PontosTuristicosViewSet(ModelViewSet):
	queryset = PontoTuristico.objects.all()
	serializer_class = PontoTuristicoSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['nome', 'enderecos__linha1']
