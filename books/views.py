from django.shortcuts import render
from __init__ import pyro
from django.shortcuts import redirect


def home(request, by_what='tytul'):
    """ Strona glowna. Parametr 'by_what' mowi nam po czym sortujemy liste. """

    if request.POST.get('search'):
        return redirect('/search/' + request.POST.get('query'))

    sort = by_what
    
    book_list = pyro.library.getBook_list(20)
    sorted_list = pyro.library.getBook_sort(by_what, 'ASC', 30)
    
    template = "index.html"
    context = {'book_list':book_list, 'sorted_list':sorted_list, 'sort':sort}

    return render(request, template, context)

def test(request):
    """ Strona testowa. """
   	
    if request.POST.get('register'):
        pyro.library.registry(request.POST.get('login'),request.POST.get('password'),request.POST.get('password2'),request.POST.get('adres'),request.POST.get('nrtel'),20)

    template = "test.html"
    context = {}

    return render(request, template, context)

def search(request, query):
    """Strona wyszukiwania"""

    if request.POST.get('search'):
        return redirect('/search/' + request.POST.get('query'))

    sorted_list = pyro.library.search(query)

    template = "search.html"
    context = {'sorted_list':sorted_list}

    return render(request, template, context)

def cart(request):
    
    cart_list = pyro.library.getCart_list(20)

    template = "cart.html"
    context = {'cart_list':cart_list }

    return render(request, template, context)

def add(request, book_id, ilosc):
    """ Dodawanie ksiazki."""

    pyro.library.addBook(book_id, ilosc)

    return redirect("/")

def delete(request, book_id):
    """ Usuwanie ksiazki."""

    print pyro.library.deleteBook(book_id)

    return redirect("/cart/")