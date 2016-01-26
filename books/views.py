from django.shortcuts import render
from __init__ import pyro
from django.shortcuts import redirect


def home(request, page=0, by_what='tytul'):
    """ Strona glowna. Parametr 'by_what' mowi nam po czym sortujemy liste. """

    page = int(page)

    if request.POST.get('search'):
        return redirect('/search/%s/%s' % (request.POST.get('query'), 0))

    if request.GET.get('next'):
        page += 1
        return redirect('/%s/%s/' % (page, by_what))

    elif request.GET.get('previous'):
        if page == 0:
            pass
        else:
            page -= 1
        return redirect('/%s/%s/' % (page, by_what))
    
    book_list = pyro.library.getBook_list(100)
    sorted_list = pyro.library.getBook_sort(by_what, 'ASC', 100, int(page))
    price = pyro.library.getBook_price()[0][0]

    template = "index.html"
    context = {'book_list':book_list, 'sorted_list':sorted_list, 'sort':by_what, 'page':page, 'price':price}

    return render(request, template, context)

def test(request):
    """ Strona testowa. """

    price = pyro.library.getBook_price()[0][0]

    if request.POST.get('register'):
        pyro.library.registry(request.POST.get('login'),request.POST.get('password'),request.POST.get('password2'),request.POST.get('adres'),request.POST.get('nrtel'),20)

    request.session['foo'] = 'bar' # tak przypisujemy wartosci do sesji
    print request.session.get('foo') # tak odczytujemy wartosci z sesji

    template = "test.html"
    context = {'price':price}

    return render(request, template, context)

def search(request, query, page):
    """Strona wyszukiwania"""

    page = int(page)

    if request.POST.get('search'):
        return redirect('/search/%s/%s' % (request.POST.get('query'), page))

    if request.GET.get('next'):
        page += 1
        return redirect('/search/%s/%s' % (query, page))

    elif request.GET.get('previous'):
        if page == 0:
            pass
        else:
            page -= 1
        return redirect('/search/%s/%s' % (query, page))

    sorted_list = pyro.library.search(query, page)

    price = pyro.library.getBook_price()[0][0]

    template = "search.html"
    context = {'sorted_list':sorted_list, 'page':page, 'price': price}

    return render(request, template, context)

def cart(request):

    cart_list = pyro.library.getCart_list(20)

    price = pyro.library.getBook_price()[0][0]

    template = "cart.html"
    context = {'cart_list':cart_list, 'price': price}

    return render(request, template, context)

def order(request):

    pyro.library.finalizeOrder(1)

    cart_list = pyro.library.getCart_list(20)

    price = pyro.library.getBook_price()[0][0]

    template = "order.html"
    context = {'cart_list':cart_list, 'price': price}

    return render(request, template, context)

def add(request, book_id, ilosc):
    """ Dodawanie ksiazki do koszyka. """

    pyro.library.addBook(book_id, ilosc)

    return redirect("/")

def delete(request, book_id):
    """ Usuwanie ksiazki z koszyka. """

    print pyro.library.deleteBook(book_id)

    return redirect("/cart/")
