from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets, permissions

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]