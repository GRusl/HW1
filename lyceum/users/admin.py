from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext_lazy as _

from users.models import Profile

User = get_user_model()


class ProfileInlined(admin.TabularInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    inlines = (ProfileInlined,)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    list_display_links = ("email",)


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
