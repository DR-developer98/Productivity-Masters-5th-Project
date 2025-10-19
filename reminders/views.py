from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reminder
from rest_framework.permissions import IsAuthenticated
from .serializers import ReminderSerializer


class ReminderList(APIView):
    """
    Return all reminders the current user has created
    """
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reminders = Reminder.objects.filter(owner=request.user)
        serializer = ReminderSerializer(
            reminders, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReminderSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReminderDetail(APIView):
    """
    Retrieve, change or delete a single reminder instance
    """
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            reminder = Reminder.objects.get(pk=pk)
            if self.request.user not in reminder.task.owners.all():
                raise Http404
            return reminder
        except Reminder.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reminder = self.get_object(pk)
        serializer = ReminderSerializer(
            reminder, context={'request': request}
            )
        return Response(serializer.data)

    def put(self, request, pk):
        reminder = self.get_object(pk)
        serializer = ReminderSerializer(reminder, data=request.data,
                                        context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reminder = self.get_object(pk)
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
