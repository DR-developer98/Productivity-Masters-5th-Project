from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer


class TaskList(APIView):
    """
    Return all tasks the current user 
    has created and allow for full CRUD 
    functionalities on the tasks records
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tasks = Task.objects.filter(owners=request.user)
        serializer = TaskSerializer(tasks, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
            task = serializer.save()
            task.owners.add(request.user) 
            # ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetail(APIView):
    """
    Retrieve, update or delete a single task item owned by the user
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk, owners=self.request.user)
            return task
        except Task.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)  
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
