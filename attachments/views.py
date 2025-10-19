from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Attachment
from .serializers import AttachmentSerializer
from drf_api.permissions import IsTaskOwner


class AttachmentList(generics.ListCreateAPIView):
    """
    List all attachments for tasks owned by the user.
    Allow uploading new attachments if the user is an owner of the task.
    """
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Attachment.objects.filter(task__owners=self.request.user)

    def perform_create(self, serializer):
        task = serializer.validated_data['task']
        if self.request.user not in task.owners.all():
            raise PermissionDenied("You may not add attachments to this task.")
        serializer.save()


class AttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a single attachment if the user is a task owner.
    """
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]

    def get_queryset(self):
        return Attachment.objects.filter(task__owners=self.request.user)
