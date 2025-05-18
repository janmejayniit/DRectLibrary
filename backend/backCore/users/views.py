from django.shortcuts import render
from rest_framework import viewsets, status
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UserSerializer
# from django.contrib.auth import get_user_model
from .models import User
from django.db import models
from django.db.models import Q


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for creating users.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # permission_classes = [IsAuthenticated]  # Only authenticated users can create new users




# User = get_user_model()

class UserLookupView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({'detail': 'Query parameter "q" is required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(
            models.Q(email__iexact=query) |
            models.Q(username__iexact=query) |
            models.Q(phone__iexact=query)
        ).first()

        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)