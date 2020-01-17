from django.db import models
from datetime import datetime



class Tutorial(models.Model):
	"""
		Base tutorial model with title, content and published date
	"""
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField("date published", default=datetime.now)

	def __str__(self):
		return self.title

