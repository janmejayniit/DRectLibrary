from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Author, Genre, Language, BookStock
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer

    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]