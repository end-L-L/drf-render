from rest_framework import routers
from .viewsets import TaskViewSet

router = routers.DefaultRouter()

router.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls