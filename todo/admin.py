from django.contrib import admin, messages
from django.utils.translation import ngettext
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Tag, Todo
from django.utils import timezone

# Register your models here.

admin.site.register(Tag)


class TodoResource(resources.ModelResource):
    tags = fields.Field(column_name="tags", attribute="tags", widget=ManyToManyWidget(Tag, field="name"))

    def before_import_row(self, row, **kwargs):
        due_date = datetime.strptime(row["due_date"], "%Y-%m-%d").date()

        if due_date < timezone.localdate():
            raise ValidationError("Due date cannot be in past")

        tags = row["tags"].split(",")
        for tag in tags:
            Tag.objects.get_or_create(name=tag.strip())

    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "description",
            "due_date",
            "created_at",
            "tags",
            "high_priority",
            "status",
        )
        export_order = fields


@admin.register(Todo)
class ToDoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Todo settings for admin panel
    """

    resource_class = TodoResource
    list_display = ["title", "status", "due_date", "created_at", "owner"]
    ordering = ["due_date"]
    readonly_fields = ("created_at",)
    search_fields = ("title__startswith",)
    search_help_text = "Search by title"
    filter_horizontal = ("tags",)
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = [
        ("Mandatory Fields", {"fields": ["owner", ("title", "due_date"), "status"]}),
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


admin.site.site_header = "Todos Administration"
admin.site.site_title = "Todos Administration"
admin.site.index_title = "Todos Admin"
