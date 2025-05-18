from rest_framework import serializers
from .models import Book, Author, Genre, Language, BookStock

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

# class BookStockSerializer(serializers.ModelSerializer):
#     available_stock = serializers.IntegerField(source='available_stock', read_only=True)
#     class Meta:
#         model = BookStock
#         fields = ['available_stock']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)
     

    # Also include the foreign key IDs to allow write operations
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), source='genre', write_only=True)
    language_id = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), source='language', allow_null=True, write_only=True)
    
    # book_stock = BookStockSerializer(many=True, read_only=True)
    total_stock = serializers.IntegerField( read_only=True)

    class Meta:
        model = Book
        # fields = '__all__'
        # fields = ['id', 'title', 'author', 'isbn', 'genre', 'description', 'publication_date', 'publisher', 'cover_image', 'total_copies', 'language', 'pages', 'price', 'rating']  # Specify the fields you want to include  
        fields = [
            'id', 'title', 'author', 'isbn', 'genre', 'description', 'publication_date', 
            'publisher', 'cover_image', 'total_copies', 'language', 'pages', 'price', 
            'rating', 'total_stock', 'author_id', 'genre_id', 'language_id'
        ]
        