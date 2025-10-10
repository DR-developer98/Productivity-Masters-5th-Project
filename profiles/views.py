from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        profiles = Profile.objects.all()
        # ↓↓↓ CREDIT: Django Rest Framework module - Code Institute ↓↓↓
        serializer = ProfileSerializer(profiles, many=True)
        # ↑↑↑ CREDIT: Django Rest Framework module - Code Institute ↑↑↑
        return Response(serializer.data)


