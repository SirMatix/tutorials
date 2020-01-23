from django.contrib import admin
from .models import News, Welcome
from tinymce.widgets import TinyMCE
from django.db import models

class NewsAdmin(admin.ModelAdmin):
    """
    class that is used to present our tutorial model in admin panel
    we are overwritting the default model structure to display
    fields in the manner defined by us
    """
    # dividing fields into fieldsets
    fieldsets = [
        ("Title/date", {"fields": ["title", "published"]}),
        ("Content", {"fields": ["content", "author"]})
    ]

    # overridding form field to include tinyMCE widget
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Welcome, NewsAdmin)