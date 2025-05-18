from django.db import models
from django.utils import timezone
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255, blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    total_copies = models.PositiveIntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    @property
    def total_stock(self):
        borrowed_count = sum(stock.quantity for stock in self.book_stock.all())
        return self.total_copies - borrowed_count

class BookStock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_stock')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} copies of {self.book.title} in stock"