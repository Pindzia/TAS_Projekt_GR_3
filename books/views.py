from django.shortcuts import render
from __init__ import pyro
from django.shortcuts import redirect

# login, password, password_2, adres, nr_Telefonu, e_Mail, rows)
def get_test():
    print library.test()


def home(request, by_what='tytul'):
    """ Strona glowna. Parametr 'by_what' mowi nam po czym sortujemy liste. """

    if request.POST.get('search'):
        return redirect('/search/' + request.POST.get('query'))

    sort = by_what
    
    book_list = pyro.library.getBook_list(20)
    sorted_list = pyro.library.getBook_sort(by_what, 'ASC', 20)
    
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

    book_list = pyro.library.getBook_list(20)
    sorted_list = pyro.library.search(query)
    print query

    template = "index.html"
    context = {'book_list':book_list, 'sorted_list':sorted_list}

    return render(request, template, context)

def cart(request):
    pass

def add(request, book_id, ilosc):
    """ Dodawanie ksiazki."""

    print "sasasdsa"

    pyro.library.addBook(book_id, ilosc)

    return redirect("/")