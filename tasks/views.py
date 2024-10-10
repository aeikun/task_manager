from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from django.utils import timezone


def api_root(request):
    return JsonResponse({"message": "Welcome to the Task Manager API"})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'Completed' if task.status == 'Pending' else 'Pending'
        task.completed_at = None if task.status == 'Pending' else timezone.now()
        task.save()
        return Response({'status': task.status})

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer