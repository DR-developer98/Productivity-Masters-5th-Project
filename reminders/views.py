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