from django.contrib import admin
from .models import Book, Author, BookInstance, Language


class InstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'imprint', 'status', 'due_back']
    list_filter = ['status', 'due_back']

admin.site.register(BookInstance, InstanceAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

admin.site.register(Language, LanguageAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'author', 'genre']
    list_filter = ['title']

admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    list_filter = ['first_name', 'last_name']

admin.site.register(Author, AuthorAdmin)

