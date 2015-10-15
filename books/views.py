from django.shortcuts import render

# Widoki - tu dzieje sie magia.

from .forms import BookForm
from .models import Book

def home(request):
    """Strona glowna."""

    addBookForm = BookForm(request.POST or None) # Form, ktory dodamy w htmlu.
    if addBookForm.is_valid(): # Sprawdz, czy wpis jest poprawny.
        new_book = addBookForm.save(commit=False)
        new_book.save() # I zapisujemy do bazy danych. To wszystko.


    template = "home.html"
    context = {"addBookForm" : addBookForm}

    return render(request, template, context)
