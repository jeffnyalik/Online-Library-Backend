from django.urls import path
from .views import (
    AllAuthorsApiView, 
    AllBooksApiView, 
    AvailableBooksApiView, 
    BookInstanceApiView, 
    BooksDetaiilView, 
    CountBooksApiView, 
    NumberAuthorsApiView,
    BooksAddApIView,
    AuthorAddApiView,
    )

urlpatterns = [
    path('count-books/', CountBooksApiView.as_view(), name='count-books'),
    path('books-status/', BookInstanceApiView.as_view(), name='books-instance'),
    path('books-available/', AvailableBooksApiView.as_view(), name='books-available'),
    path('num-authors/', NumberAuthorsApiView.as_view(), name='num-authors'),
    path('all-authors/', AllAuthorsApiView.as_view(), name='all-authors'),
    path('all-books/', AllBooksApiView.as_view(), name='all-books'),
    path('add-book/',  BooksAddApIView.as_view(), name='add-book'),
    path('single-book/<int:pk>/', BooksDetaiilView.as_view(), name='single-book'),
    path('add-author/', AuthorAddApiView.as_view(), name='add-author'),

]
