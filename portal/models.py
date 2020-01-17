from django.db import models
from django.utils import timezone
import datetime

class Area(models.Model):
	descricao = models.CharField(max_length=200, blank=False)
	cor = models.CharField(max_length=200, blank=False)
	status = models.BooleanField(blank=False)

	def __str__(self):
		return self.descricao

	def ativar(self):
		self.status = True
		self.save()	

	def desativar(self):
		self.status = False
		self.save()


class Noticia(models.Model):
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	area = models.ForeignKey('Area', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200, null=False, blank=False)
	foto = models.ImageField(upload_to='images/', null=True, blank=True)
	texto = models.TextField(null=False, blank=False)
	data_de_criacao = models.DateTimeField(default=timezone.now)
	data_de_publicacao = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.titulo

	def publicar(self):
		self.data_de_publicacao = timezone.now()
		self.save()