# region				-----External Imports-----
from rest_framework.serializers import (
    ModelSerializer, Serializer
)
from typing import List, Dict, Any
# endregion

# region				-----Internal Imports-----
from ..models import (
    Todo, Step, Group
)
# endregion


class TodoSerializer(ModelSerializer):

    class Meta(object):
        model = Todo
        fields = ["id", "title", "description", "is_important",
                  "archived", "type", "created_at", "update_at"]


class TodoPreviewSerializer(Serializer):
    # region			-----Internal Methods-----
    def to_representation(self, instance) -> Dict:
        representation = super(TodoPreviewSerializer, self) \
            .to_representation(instance=instance)

        representation["id"] = instance.id
        representation["title"] = instance.title
        representation["type"] = instance.Type
        representation["is_important"] = instance.is_important

        return representation
    # endregion


class StepSerializer(ModelSerializer):

    class Meta(object):
        model = Step
        fields = ["id", "title", "type"]


class GroupSerializer(ModelSerializer):

    class Meta(object):
        model = Group
        fields = ["id", "todos", "title"]


class GroupPreviewSerializer(Serializer):
    # region			-----Internal Methods-----
    def to_representation(self, instance) -> Dict:
        representation = super(GroupPreviewSerializer, self) \
            .to_representation(instance=instance)

        representation["id"] = instance.id
        representation["title"] = instance.title

        return representation
    # endregion
