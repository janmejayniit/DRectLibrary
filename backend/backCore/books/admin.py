from django.contrib import admin
from .models import Book, Author, Genre, Language, BookStock
# Register your models here.

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Language)
# admin.site.register(Book)
admin.site.register(BookStock)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'language', 'publication_date', 'price')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'isbn')
    list_filter = ('genre', 'language', 'publication_date')
