from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=255)
	group = models.CharField(max_length=32)
