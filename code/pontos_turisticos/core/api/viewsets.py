from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontosTuristicosViewSet(ModelViewSet):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	queryset = PontoTuristico.objects.all()
	serializer_class = PontoTuristicoSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['nome','cidade','estado']

	def perform_create(self, serializer):
		serializer.save(cadastrado_por=self.request.user)