from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Borrow
from .serializers import BorrowSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class BorrowViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        # # if user.role == 'admin' or user.role == 'librarian':
        # #     return Borrow.objects.all()
        # return Borrow.objects.filter(user=user)
        return Borrow.objects.all().order_by('-borrow_date')
    
class BorrowDetailViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowSerializer

    def get_queryset(self):
        return Borrow.objects.all()

    def get_object(self):
        user_id = self.kwargs.get('user')
        book_id = self.kwargs.get('book')
        return get_object_or_404(Borrow, user__id=user_id, book__id=book_id)

    @action(detail=True, methods=['post'], url_path='issue')
    def issue_book(self, request, user=None, book=None):
        if Borrow.objects.filter(user_id=user, book_id=book, return_date=None).exists():
            return Response({"error": "User has already borrowed this book."}, status=status.HTTP_400_BAD_REQUEST)

        borrow = Borrow.objects.create(user_id=user, book_id=book)
        serializer = self.get_serializer(borrow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='return')
    def return_book(self, request, user=None, book=None):
        borrow = self.get_object()
        borrow.returned = True
        borrow.save()
        return Response({"message": "Book returned successfully."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='renew')
    def renew_book(self, request, user=None, book=None):
        borrow = self.get_object()
        # Implement your renewal logic here (e.g., extend due date)
        return Response({"message": "Book renewed successfully."}, status=status.HTTP_200_OK)