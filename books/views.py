from django.shortcuts import render
from __init__ import pyro


def get_test():
    print library.test()


def home(request):
    """Strona glowna."""

    # addBookForm = BookForm(request.POST or None) # Form, ktory dodamy w htmlu.
    # if addBookForm.is_valid(): # Sprawdz, czy wpis jest poprawny.
    #     new_book = addBookForm.save(commit=False)
    #     new_book.save() # I zapisujemy do bazy danych. To wszystko.
    # books = Book.objects.all()
    
    ev = pyro.library.test() # tak odnosimy sie metod zawartych w pliku Pyro/library.py. Wystarczy przypisywac je do zmiennych, rejestrowac w "context" i mozemy je wyswietlac na stronie.


    template = "index.html"
    context = {'ev':ev}

    return render(request, template, context)
