from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Attachment
from .serializers import AttachmentSerializer


class AttachmentList(APIView):
    """
    List all attachments for tasks owned by the user
    Allow uploading new attachments
    """
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attachments = Attachment.objects.filter(task__owners=request.user)
        serializer = AttachmentSerializer(attachments, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = AttachmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            task = serializer.validated_data['task']
            if request.user not in task.owners.all():
                return Response({'detail': 'You may not add attachments to this task.'}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)