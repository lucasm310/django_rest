from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from enderecos.models import Enderecos
from user.models import CustomUser

class PontoTuristico(models.Model):
	"""Model definition for PontoTurisico."""
	nome = models.CharField(max_length=50)
	descricao = models.TextField()
	aprovado = models.BooleanField(default=False)
	atracoes = models.ManyToManyField(Atracoes)
	comentarios = models.ManyToManyField(Comentarios)
	avaliacoes = models.ManyToManyField(Avaliacoes)
	enderecos = models.ForeignKey(
		Enderecos, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=True
	)
	cadastrado_por = models.ForeignKey(
		CustomUser,
		on_delete=models.CASCADE,
		editable=False
	)
	data_cadastro = models.DateTimeField(auto_now_add=True)
	# foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)


	def __str__(self):
		"""Unicode representation of PontoTurisico."""
		return self.nome