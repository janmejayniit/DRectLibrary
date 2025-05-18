from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Book, Author, Genre, Language, BookStock
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__first_name', 'author__last_name', 'genre__name', 'language__name']
    filterset_fields = ['author', 'genre', 'language']
    # permission_classes = [IsAuthenticatedOrReadOnly]