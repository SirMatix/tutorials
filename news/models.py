from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField(default=datetime.now)
	author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	class Meta:
	# gives the proper plural name for admin
		verbose_name_plural ="News"

	def __str__(self):
		return self.title

class Welcome(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField(default=datetime.now)
	author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	class Meta:
	# gives the proper plural name for admin
		verbose_name_plural ="Welcome"

	def __str__(self):
		return self.title