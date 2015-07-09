from django.db import models

# Create your models here.

class Article(models.Model):
	title       = models.CharField(max_length=255)
	group       = models.CharField(max_length=32)
    instime     = models.DateTimeField(auto_now=True)
    uptime      = modles.DateTimeField(auto_now=True)
    content     = modles.TextField()
    tags        = modles.CharField(max_length=255)
    author      = models.CharField(max_length=64)

    def __unicode__(self):
        return '%s by %s' %(self.name, self.author)