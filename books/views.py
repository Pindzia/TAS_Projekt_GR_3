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
    
    ev = pyro.library.test() # tak odnosimy sie do metod zawartych w pliku PyRo/library.py. Wystarczy przypisywac je do zmiennych, rejestrowac w "context" i mozemy je wyswietlac na stronie.
    example_book = pyro.library.getBook_id('9')
    book_list = pyro.library.getBook_list(20)
    sorted_list = pyro.library.getBook_sort('cena', 'ASC', 20)

    template = "index.html"
    context = {'ev':ev, 'example_book':example_book, 'book_list':book_list, 'sorted_list':sorted_list}

    return render(request, template, context)
