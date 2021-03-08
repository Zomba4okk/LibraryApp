from django.contrib import admin

from apps.books.models import Book, BookLendingLog

admin.site.register(Book)
admin.site.register(BookLendingLog)
