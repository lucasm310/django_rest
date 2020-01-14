from django.db import models
from core.models import PontoTuristico

class Atracoes(models.Model):
	"""Model definition for Atracoes."""
	ponto_turistico = models.ForeignKey(PontoTuristico,  related_name='atracoes', on_delete=models.CASCADE)
	nome = models.CharField(max_length=50)
	descricao = models.TextField()
	horario_func = models.TextField()
	idade_minima = models.IntegerField()
	# foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

	def __str__(self):
		return self.nome