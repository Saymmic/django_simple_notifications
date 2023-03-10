import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer

from .models import Notification


# Register your models here.
@admin.register(Notification)
class NotificationHistoryAdmin(admin.ModelAdmin):
    fields = ["uuid", "type", "status", "created_at", "sent_at", "pretty_details"]
    list_display = ["uuid", "type", "status", "created_at", "sent_at"]
    search_fields = ["uuid", "created_at", "sent_at", "details"]
    list_filter = ["status", "type"]
    ordering = ["-created_at"]
    readonly_fields = ["uuid", "type", "status", "created_at", "sent_at", "pretty_details"]

    @admin.display()
    def pretty_details(self, instance: Notification) -> str:
        """Function to display pretty version of json"""

        # Convert the data to sorted, indented JSON
        response = json.dumps(instance.details, sort_keys=True, indent=2)

        # Get the Pygments formatter
        formatter = HtmlFormatter(style="colorful")

        # Highlight the data
        response = highlight(response, JsonLexer(), formatter)

        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        # Safe the output
        return mark_safe(style + response)
