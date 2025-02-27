from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    search_word = "book"  # Replace with the actual word or retrieve from request.GET

    # Count books containing the search word (case insensitive)
    num_books_containing_word = Book.objects.filter(title__icontains=search_word).count()

    # Count genres containing the search word (case insensitive)
    num_genres_containing_word = Genre.objects.filter(name__icontains=search_word).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_containing_word': num_books_containing_word,
        'num_genres_containing_word': num_genres_containing_word,
        'search_word': search_word,  # Optional: Pass the word to the template
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)