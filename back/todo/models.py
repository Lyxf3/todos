# region                -----External Imports-----
from django.db import models
from django.utils import timezone
# endregion

# region                -----Internal Imports-----
from .choices import todo_types
# endregion


class Todo(models.Model):
    # region                -----Relations-----
    user = models.ForeignKey(to="user.User",
                             blank=False,
                             null=False,
                             on_delete=models.CASCADE,
                             related_name="todos",
                             verbose_name="User")
    # endregion

    # region                -----Information-----
    title = models.CharField(max_length=30,
                             null=True,
                             verbose_name="Title")

    description = models.TextField(null=True,
                                   verbose_name="Description")

    is_important = models.BooleanField(default=False,
                                       verbose_name="Is important")

    archived = models.BooleanField(default=False,
                                   verbose_name="Archived")

    type = models.PositiveIntegerField(blank=False,
                                       null=True,
                                       choices=todo_types,
                                       verbose_name="Type")

    created_at = models.DateTimeField(default=timezone.now,
                                      verbose_name="Created at")

    update_at = models.DateTimeField(default=timezone.now,
                                     verbose_name="Update at")
    # endregion

    # region         -----Default Methods-----
    def __str__(self) -> str:
        return self.title
    # endregion


class Step(models.Model):
    # region                -----Relations-----
    todo = models.ForeignKey(to="todo.Todo",
                             blank=False,
                             null=False,
                             on_delete=models.CASCADE,
                             related_name="step",
                             verbose_name="Todo")
    # endregion

    # region                -----Information-----
    title = models.CharField(max_length=30,
                             null=True,
                             verbose_name="Title")

    type = models.BooleanField(default=False,
                               verbose_name="Type")
    # endregion

    # region         -----Default Methods-----
    def __str__(self) -> str:
        return self.title
    # endregion


class Group(models.Model):
    # region           -----Relation-----
    user = models.ForeignKey(to="user.User",
                             blank=False,
                             null=False,
                             on_delete=models.CASCADE,
                             related_name="group",
                             verbose_name="User")

    todos = models.ForeignKey(to="todo.Todo",
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              related_name="group",
                              verbose_name="Todos")
    # endregion
    # region                -----Information-----
    title = models.CharField(max_length=30,
                             blank=True,
                             null=True,
                             verbose_name="Title")
    # endregion

    # region         -----Default Methods-----
    def __str__(self) -> str:
        return self.title
    # endregion
