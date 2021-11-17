# region				-----External Imports-----
from rest_framework import generics, permissions, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from typing import List, Dict
# endregion

# region				-----Internal Imports-----
from .serializers import UserSerializer
from ..models import User
# endregion


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
