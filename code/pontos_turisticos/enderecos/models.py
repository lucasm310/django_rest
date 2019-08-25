from django.db import models

class Enderecos(models.Model):
	"""Model definition for Enderecos."""
	linha1 = models.CharField(max_length=150)
	linha2 = models.CharField(max_length=150, null=True, blank=True)
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	latitude = models.IntegerField(null=True, blank=True)
	longitude = models.IntegerField(null=True, blank=True)

	class Meta:
		"""Meta definition for Enderecos."""

		verbose_name = 'Enderecos'
		verbose_name_plural = 'Enderecos'

	def __str__(self):
		"""Unicode representation of Enderecos."""
		return self.linha1