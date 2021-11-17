# region				-----External Imports-----
from rest_framework import generics, permissions, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from typing import List, Dict
# endregion

# region				-----Internal Imports-----
from .serializers import (
    TodoSerializer, StepSerializer, GroupSerializer,
    TodoPreviewSerializer, GroupPreviewSerializer
)
from ..models import (
    Todo, Step, Group
)
from user.models import User
# endregion


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def _prefetch_todos(self, queryset):
        queryset = queryset.select_related("steps")

        return queryset

    def list(self, request):
        user_id = request.user.pk
        todos = Todo.objects.filter(user__id=user_id)


        return Response(
            data=TodoPreviewSerializer(
                instance=todos,
                many=True
            ).data
        )

    def retrieve(self, request, pk=None):
        todo = self._prefetch_chats(queryset= \
                                        Todo.objects \
                                    .filter(pk=pk)
                                    )

        return Response(
            data=TodoSerializer(
                instance=todo,
                many=False
            ).data
        )

    def create(self, request):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        todo_id = self.request.query_params.get("todo_id")
        steps = Step.objects.filter(todo__id=todo_id)

        return Response(
            data=StepSerializer(
                instance=steps,
                many=True
            ).data
        )

    def create(self, request):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def _prefetch_groups(self, queryset):
        queryset = queryset \
            .select_related("todos") \
            .only("id", "title", "todos")

        return queryset

    def list(self, request):
        user_id = request.user.pk
        groups = Group.objects. \
            filter(user__id=user_id) \
            .only("id", "title")

        return Response(
            data=GroupPreviewSerializer(
                instance=groups,
                many=True
            ).data
        )

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        group = self._prefetch_groups(queryset= \
                                          Group.objects.filter(pk=pk))

        return Response(
            data=GroupSerializer(
                instance=group,
                many=False
            ).data
        )

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
