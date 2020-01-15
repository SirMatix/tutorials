from django.db import models



class Tutorial(models.Model):
	"""
		Base tutorial class with title, content and published date
	"""
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField("date published")

	def __str__(self):
		return self.title