from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Borrow
from books.models import BookStock

@receiver(post_save, sender=Borrow)
def update_book_stock_on_borrow(sender, instance, created, **kwargs):
    if created:
        stock = BookStock.objects.filter(book=instance.book).first()
        if stock and stock.quantity > 0:
            stock.quantity += 1
            stock.save()   
        else:
            BookStock.objects.create(book=instance.book, quantity=1)


@receiver(pre_save, sender=Borrow)
def restore_stock_on_return(sender, instance, **kwargs):
    if not instance.pk:
        return  # New record, no prior state

    try:
        previous = Borrow.objects.get(pk=instance.pk)
    except Borrow.DoesNotExist:
        return

    if previous.return_date is None and instance.return_date is not None:
        stock = BookStock.objects.filter(book=instance.book).first()
        if stock and stock.quantity > 0:
            stock.quantity -= 1
            stock.save()
        else:
            print(f"[ERROR] No BookStock found to restore for returned book: {instance.book}")