# region				-----External Imports-----
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.serializers import ModelSerializer, SerializerMethodField, Serializer
from rest_framework_simplejwt.tokens import RefreshToken
from typing import List, Dict, Any
# endregion

# region				-----Internal Imports-----
from ..models import User
# endregion


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "first_name", "second_name", "email",
                  "sex", "about"]


class UserRegisterSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "email", "first_name", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

        # region      -----Internal Methods-----
        def create(self, validated_data):
            user = User.objects.create(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user
        # endregion


class UserPreviewSerializer(Serializer):
    # region			-----Internal Methods-----
    def to_representation(self, instance) -> Dict:
        representation = super(UserPreviewSerializer, self) \
            .to_representation(instance=instance)

        representation["id"] = instance.id
        representation["first_name"] = instance.first_name
        representation["email"] = instance.email

        return representation
    # endregion