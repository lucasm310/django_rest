from users.models import CustomUser
from django.db import models

class Avaliacoes(models.Model):
	"""Model definition for Avaliacoes."""
	usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	comentario = models.TextField(null=True, blank=True)
	nota = models.DecimalField(max_digits=3, decimal_places=2)
	data = models.DateField(auto_now_add=True)	

	class Meta:
		"""Meta definition for Avaliacoes."""

		verbose_name = 'Avaliacoes'
		verbose_name_plural = 'Avaliacoes'

	def __str__(self):
		"""Unicode representation of Avaliacoes."""
		return self.usuario.username
