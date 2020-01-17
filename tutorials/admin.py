from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models


class TutorialAdmin(admin.ModelAdmin):
    """
    class that is used to present our tutorial model in admin panel
    we are overwritting the default model structure to display
    fields in the manner defined by us
    """
    # dividing fields into fieldsets
    fieldsets = [
        ("Title/date", {"fields": ["title", "published"]}),
        ("Content", {"fields": ["content"]})
    ]

    # overridding form field to include tinyMCE widget
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


# Registering models

admin.site.register(Tutorial, TutorialAdmin)

