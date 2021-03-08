from datetime import datetime

from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from apps.books.models import Book, BookLendingLog
from apps.books.permissions import StaffUserPermissionMixin
from apps.books.forms import BookLendForm


class BooksListView(LoginRequiredMixin, ListView):
    queryset = Book.objects.prefetch_related('logs__user')
    template_name = 'books_list.html'
    context_object_name = 'books'


class BookLendView(StaffUserPermissionMixin, View):
    def get(self, request, book_id, *args, **kwargs):
        book = get_object_or_404(Book, id=book_id)

        return render(
            request,
            'book_lending.html',
            {'form': BookLendForm(), 'book_name': str(book)}
        )

    def post(self, request, book_id, *args, **kwargs):
        book = get_object_or_404(Book, id=book_id)

        if book.is_available:
            BookLendingLog.objects.create(book=book, user=request.user)

            return redirect('main_page')
        return HttpResponseBadRequest()


class BookReturnView(StaffUserPermissionMixin, View):
    def post(self, request, book_id, *args, **kwargs):
        book_lending_log = (
            BookLendingLog.objects
            .filter(book_id=book_id, returning_date__isnull=True)
            .first()
        )

        if book_lending_log:
            book_lending_log.returning_date = datetime.now()
            book_lending_log.save()

            return redirect('main_page')
        return HttpResponseBadRequest()

