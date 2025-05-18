from rest_framework import serializers
from .models import Borrow
from books.serializers import BookSerializer
from books.models import Book, BookStock
from users.serializers import UserSerializer

class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book', write_only=True)
    # user = serializers.ReadOnlyField(source='user.username')
    user = UserSerializer(read_only=True)  # Add this line
    class Meta:
        model = Borrow
        fields = ['id', 'user', 'book', 'book_id', 'borrow_date', 'due_date', 'return_date', 'fine', 'is_overdue', 'user_have_borrowed', 'has_unreturned_books']
        read_only_fields = ['borrow_date', 'fine', 'is_overdue', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        book = validated_data['book']
        stock = BookStock.objects.filter(book=book).first()

        if not stock or stock.quantity <= 0:
            raise serializers.ValidationError("This book is currently out of stock.")

        validated_data['user'] = user
        return super().create(validated_data)
