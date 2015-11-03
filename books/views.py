from django.shortcuts import render
from .forms import BookForm
from .models import Book

# Widoki - tu dzieje sie magia.


def home(request):
    """Strona glowna."""

    addBookForm = BookForm(request.POST or None) # Form, ktory dodamy w htmlu.
    if addBookForm.is_valid(): # Sprawdz, czy wpis jest poprawny.
        new_book = addBookForm.save(commit=False)
        new_book.save() # I zapisujemy do bazy danych. To wszystko.

    books = Book.objects.all()
    
    template = "home.html"
    context = {"addBookForm":addBookForm, "books":books}

    return render(request, template, context)


# SKUP sie na interfejsach zdalnych
# PyRo