from django.shortcuts import render
import Pyro4
# from .forms import BookForm
# from .models import Book

# Widoki - tu dzieje sie magia.


def runpyro():
    uri = input("Enter the uri of the library: ").strip()
    library = Pyro4.Proxy(uri)
    print "PyRo is running..."

def get_test():
    print library.test()

def home(request):
    """Strona glowna."""

    # addBookForm = BookForm(request.POST or None) # Form, ktory dodamy w htmlu.
    # if addBookForm.is_valid(): # Sprawdz, czy wpis jest poprawny.
    #     new_book = addBookForm.save(commit=False)
    #     new_book.save() # I zapisujemy do bazy danych. To wszystko.

    # books = Book.objects.all()

    ev = "VAR"
    
    template = "index.html"
    context = {'ev':ev}

    return render(request, template, context)
