# region				-----External Imports-----
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# endregion

# region				-----Internal Imports-----
from .views import UserViewSet
# endregion


router = DefaultRouter()
router.register(r'user',
                UserViewSet,
                basename="user")

urlpatterns = router.urls