from rest_framework import serializers
from rest_framework.utils.model_meta import _get_reverse_relationships

from catalog.models import Author, Book, Genre


class GenreSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'books']


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerialzer(read_only=True, many=True)
    author = AuthorSerializer()
    class Meta:
        fields = '__all__'
        model = Book

