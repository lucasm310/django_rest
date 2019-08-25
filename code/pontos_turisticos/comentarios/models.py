from user.models import CustomUser
from django.db import models

class Comentarios(models.Model):
	"""Model definition for Comentarios."""
	usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	comentario = models.TextField()
	data = models.DateField(auto_now_add=True)
	aprovado = models.BooleanField(default=True)

	class Meta:
		"""Meta definition for Comentarios."""

		verbose_name = 'Comentarios'
		verbose_name_plural = 'Comentarios'

	def __str__(self):
		"""Unicode representation of Comentarios."""
		return self.usuario.username
