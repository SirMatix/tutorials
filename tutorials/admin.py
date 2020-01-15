from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
	"""
	class that is used to present our tutorial model in admin panel
    we are overwritting the default model structure to display
    fields in the manner defined by us
	"""
	fields = ["title",
              "published",
              "content"]


# Registering models

admin.site.register(Tutorial, TutorialAdmin)
