from django.db import models
from django.conf import settings
from books.models import Book
from datetime import timedelta, date
from decimal import Decimal
from django.utils import timezone

# Create your models here.

class Borrow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    @property
    def is_overdue(self):
        return self.return_date is None and date.today() > self.due_date

    @property
    def user_have_borrowed(self):
        # Check if the user has already borrowed this book
         
        return Borrow.objects.filter(
            user=self.user,
            book=self.book,
            return_date__isnull=False
        ).exists()
    
    @property
    def has_unreturned_books(self):
        return Borrow.objects.filter(user=self.user, return_date__isnull=True).exists()
    
    def save(self, *args, **kwargs):
        # Ensure borrow_date is set
        if not self.borrow_date:
            self.borrow_date = timezone.now()

        # Set due date (as a date) if not already set
        if not self.due_date:
            self.due_date = (self.borrow_date + timedelta(days=14)).date()

        # Calculate fine if book is returned late
        if self.return_date and self.return_date > self.due_date:
            days_overdue = (self.return_date - self.due_date).days
            self.fine = Decimal(days_overdue * 5)
        else:
            self.fine = Decimal('0.00')

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.username}"
