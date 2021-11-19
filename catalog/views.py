from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from serializers.catalog.serializer import AuthorSerializer, BookSerializer
from .models import BookInstance, Book, Author
from rest_framework.response import Response
from rest_framework import status



class CountBooksApiView(APIView):
    def get(self, request, format=None):
        num_books = Book.objects.all().count()
        context = {
            'status': status.HTTP_200_OK,
            'num_books': num_books
        }
        return Response(context)


class BookInstanceApiView(APIView):
    def get(self, request, format=None):
        book_instance = BookInstance.objects.all().values()

        context = {
            'status': status.HTTP_200_OK,
            'available_books': book_instance
        }
        return Response(context)

class AvailableBooksApiView(APIView):
    def get(self, request, format=None):
        book_instance = BookInstance.objects.filter(status__exact='a').count()
        context = {
            'status': status.HTTP_200_OK,
            'available_books': book_instance
        }
        return Response(context)
        

class NumberAuthorsApiView(APIView):
    def get(self, request, format=None):
        num_authors = Author.objects.count()
        context = {
            'status': status.HTTP_200_OK,
            'num_authors': num_authors
        }
        return Response(context)


class AllAuthorsApiView(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllBooksApiView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BooksDetaiilView(APIView):
    def get(self, format=None, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)