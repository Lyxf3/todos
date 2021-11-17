# region                -----External Imports-----
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.html import format_html
# endregion

# region                -----Internal Imports-----
from .models import User
# endregion


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "is_active", "password", "is_staff",
                    "first_name", "second_name", "sex", "about"]
    search_fields = ["email"]
    readonly_fields = ["password"]

    def get_queryset(self, request):
        query_set = super(UserAdmin, self).get_queryset(request)

        return query_set\
            .select_related("todos") \
            .select_related("groups")

