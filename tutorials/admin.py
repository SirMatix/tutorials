from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory #TutorialLanguage
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
        ("URL", {"fields": ["slug"]}),
        ("Series", {"fields": ["series"]}),
        ("Content", {"fields": ["content"]})
    ]

    # overridding form field to include tinyMCE widget
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


# Registering models

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
#admin.site.register(TutorialLanguage)
admin.site.register(Tutorial, TutorialAdmin)

