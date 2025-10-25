from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks assigned to the current user.
    Allow creating new tasks and automatically assign the user as one
    of the owners.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = (
        'owners__username',
        'title',
        'description',
        'due_date',
        'category__name',
    )

    def get_queryset(self):
        return Task.objects.filter(owners=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save()
        task.owners.add(self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a single task if the user is one of the owners.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Task.objects.filter(owners=self.request.user)
