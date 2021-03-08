from django.urls import path

from apps.books.views import BooksListView, BookReturnView, BookLendView


urlpatterns = [
    path('list/', BooksListView.as_view(), name='books_list'),
    path('lend/<int:book_id>/', BookLendView.as_view(), name='lend_book'),
    path('return/<int:book_id>/', BookReturnView.as_view(), name='return_book')
]