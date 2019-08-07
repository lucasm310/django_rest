from django.db import models

class Atracoes(models.Model):
	"""Model definition for Atracoes."""
	nome = models.CharField(max_length=50)
	descricao = models.TextField()
	horario_func = models.TextField()
	idade_minima = models.IntegerField()

	def __str__(self):
		return self.nome