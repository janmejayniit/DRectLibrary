from django.db import models
from django.conf import settings
from books.models import Book
from datetime import timedelta, date

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

    def save(self, *args, **kwargs):
        # Set due date if not provided
        if not self.due_date:
            self.due_date = self.borrow_date + timedelta(days=14)

        # Calculate fine when book is returned
        if self.return_date and self.return_date > self.due_date:
            days_overdue = (self.return_date - self.due_date).days
            self.fine = days_overdue * 5  # Example: ₹5 per day
        else:
            self.fine = 0.00

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.username}"
