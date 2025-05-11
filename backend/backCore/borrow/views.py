from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Borrow
from .serializers import BorrowSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class BorrowViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin' or user.role == 'librarian':
            return Borrow.objects.all()
        return Borrow.objects.filter(user=user)