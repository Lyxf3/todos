# region                -----External Imports-----
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.html import format_html
# endregion

# region                -----Internal Imports-----
from .models import (
    Todo, Step, Group
)
# endregion


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_important', 'archived',
                    'type', 'created_at', 'update_at']
    search_fields = ['title']
    fields = ["title", "description", "is_important", "archived"]
    readonly_fields = ['type', 'created_at', 'update_at']

    def get_queryset(self, request):
        query_set = super(TodoAdmin, self).get_queryset(request)

        return query_set.select_related('steps')


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    search_fields = ['title']
    fields = ["title"]
    readonly_fields = ['type']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'todos']
    search_fields = ['title']
    fields = ["title"]

    def get_queryset(self, request):
        query_set = super(GroupAdmin, self).get_queryset(request)

        return query_set.select_related('todos')
