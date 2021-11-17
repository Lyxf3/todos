# region				-----External Imports-----
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# endregion

# region				-----Internal Imports-----
from .views import (
    TodoViewSet, StepViewSet, GroupViewSet
)
# endregion


router = DefaultRouter()
router.register(r'todo',
                TodoViewSet,
                basename="todo")
router.register(r'step',
                StepViewSet,
                basename="step")
router.register(r'group',
                GroupViewSet,
                basename="group")

urlpatterns = router.urls