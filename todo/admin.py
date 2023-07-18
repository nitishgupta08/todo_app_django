from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Tag, Todo

# Register your models here.

admin.site.register(Tag)


@admin.register(Todo)
class ToDoAdmin(admin.ModelAdmin):
    """
    Todo settings for admin panel
    """
    list_display = ["title", "status", "due_date", "created_at"]
    ordering = ["due_date"]
    readonly_fields = ("created_at",)
    search_fields = ("title__startswith",)
    search_help_text = "Search by title"
    filter_horizontal = ("tags",)
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = [
        ("Mandatory Fields", {"fields": [("title", "due_date"), "status"]}),
        ("Optional Fields", {"fields": ["description", "tags"]}),
        ("Created At", {"fields": ["created_at"]}),
    ]
    list_filter = ["status", "tags"]

    actions = ["status_done"]

    @admin.action(description="Update status of selected as DONE")
    def status_done(self, request, queryset):
        """
        Added action that allows user to mark multiple tasks as done
        """
        updated = queryset.update(status="DONE")
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


admin.site.site_header = "AlgoBulls Todos Administration"
admin.site.site_title = "AlgoBulls Administration"
admin.site.index_title = "Todos Admin"
