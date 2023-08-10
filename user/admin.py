from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class UserAdmin(UserAdmin):
    list_display = ["email", "username", "is_superuser", "date_joined"]
    readonly_fields = ("password", "date_joined", "last_login")
    search_fields = ("email__icontains",)
    search_help_text = "Search by Email"
    # radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = [
        (
            "Personal Info",
            {
                "fields": [
                    "email",
                    "username",
                    ("first_name", "last_name"),
                    "password",
                    "profile_image",
                    "last_login",
                    "date_joined",
                ]
            },
        ),
        ("Permissions", {"fields": ["is_staff", "is_active", "is_superuser"]}),
    ]
    list_filter = ["is_staff"]


admin.site.register(CustomUser, UserAdmin)
