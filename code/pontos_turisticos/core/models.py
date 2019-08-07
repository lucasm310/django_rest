from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from enderecos.models import Enderecos

class PontoTuristico(models.Model):
	"""Model definition for PontoTurisico."""
	nome = models.CharField(max_length=50)
	descricao = models.TextField()
	aprovado = models.BooleanField(default=False)
	atracoes = models.ManyToManyField(Atracoes)
	comentarios = models.ManyToManyField(Comentarios)
	avaliacoes = models.ManyToManyField(Avaliacoes)
	enderecos = models.ManyToManyField(Enderecos)


	def __str__(self):
		"""Unicode representation of PontoTurisico."""
		return self.nome