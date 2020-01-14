from django.db import models
from users.models import CustomUser

class PontoTuristico(models.Model):
	"""Model definition for PontoTurisico."""
	nome = models.CharField(max_length=50)
	descricao = models.TextField()
	aprovado = models.BooleanField(default=False)
	linha1 = models.CharField(max_length=150, null=True, blank=True)
	linha2 = models.CharField(max_length=150, null=True, blank=True)
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	latitude = models.IntegerField(null=True, blank=True)
	longitude = models.IntegerField(null=True, blank=True)
	cadastrado_por = models.ForeignKey(
		CustomUser,
		on_delete=models.CASCADE
	)
	data_cadastro = models.DateTimeField(auto_now_add=True)
	# foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)


	def __str__(self):
		"""Unicode representation of PontoTurisico."""
		return self.nome