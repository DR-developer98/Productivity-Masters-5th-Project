from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderList(generics.ListCreateAPIView):
    """
    List all reminders created by the current user.
    Allow creating new reminders, automatically assigning the logged-in user as owner.
    """
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a single reminder instance.
    Access is only allowed if the user is the owner of the reminder.
    If the reminder is linked to a task, the user must be one of the task's owners.
    """
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        reminder = self.get_object()
        if reminder.task and self.request.user not in reminder.task.owners.all():
            raise PermissionDenied("You may not modify this reminder.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.task and self.request.user not in instance.task.owners.all():
            raise PermissionDenied("You may not delete this reminder.")
        instance.delete()
