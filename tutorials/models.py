from django.db import models
from datetime import datetime



# class TutorialLanguage(models.Model):
# 	language = models.CharField(max_length=200)
# 	slug = models.CharField(max_length=200, default=1)

# 	class Meta:
# 		# gives the proper plural name for admin
# 		verbose_name_plural ="Languages"

# 	def __str__(self):
# 		return self.language



class TutorialCategory(models.Model):
	category = models.CharField(max_length=200)
	#language = models.ForeignKey(TutorialLanguage, default=1, verbose_name="Language", on_delete=models.SET_DEFAULT)
	summary = models.CharField(max_length=200)
	slug = models.CharField(max_length=200, default=1)

	class Meta:
		# gives the proper plural name for admin
		verbose_name_plural ="Categories"

	def __str__(self):
		return self.category


class TutorialSeries(models.Model):
	series = models.CharField(max_length=200)
	category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	summary = models.CharField(max_length=200)

	class Meta:
		# gives the proper plural name for admin
		verbose_name_plural ="Series"

	def __str__(self):
		return self.series


class Tutorial(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField("date published", default=datetime.now)
	series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.title

