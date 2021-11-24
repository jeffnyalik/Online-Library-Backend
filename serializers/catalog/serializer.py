from rest_framework import serializers
from rest_framework.utils.model_meta import _get_reverse_relationships

from catalog.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'books']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    class Meta:
        fields = ['id','title', 'isbn', 'summary', 'author', 'genre', 'status']
        model = Book

