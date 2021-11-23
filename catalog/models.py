from django.db import models
import uuid # Required for unique book instances
from auths.models import CustomUser

class Language(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Languages'
    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}"


class Book(models.Model):
    GENRES = (
        ('Political', 'Political'),
        ('Religion', 'Religion'),
        ('Fictions', 'Fictions'),
        ('Drama', 'Drama'),
        ('Adventure', 'Adventure'),
        ('Literature', 'Literature'),
        ('Actions', 'Actions'),
    )

    BOOK_STATUS = (
        ('Unavailable', 'Unavailable'),
        ('Reserved', 'Reserved'),
        ('Available', 'Available'),
        
    )

    title = models.CharField(blank=True, null=True, max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(blank=True, default="Description")
    isbn = models.CharField(max_length=200, unique=True)
    genre = models.CharField(max_length=100, choices=GENRES, default='Fiction', blank=True, null=True)
    status = models.CharField(max_length=100, choices=BOOK_STATUS, default='Unavailable', blank=True)

    class Meta:
        verbose_name_plural = 'Books'
    
    def __str__(self) -> str:
        return self.title

   
class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True, blank=True, related_name='books')
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True, null=True)
    borrower = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='borrower')

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'