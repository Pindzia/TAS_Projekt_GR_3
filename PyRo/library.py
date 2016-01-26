# -*- coding: utf-8 -*-

import Pyro4
import database
import re
from Crypto.Hash import SHA256


class Library(object):
    """ Zawiera metody odpytujace baze danych. """

    def __init__(self):
        pass

    def test(self):
        return "Test przeszedl pomyslnie."

    def getBook_id(self, id):
        """ Zwraca ksiazke z podanym id. """
        """ mysql.check przepuszcza zmienna przez regex'a który sprawdza czy id nie ma w sobie znaków specjalnych  """
        if mysql.check(id):
            try:
                return mysql.get("SELECT idKsiazka, tytul, autor, cena, dict_img, kategoria FROM Ksiazka WHERE idKsiazka=%s;" % (id), 1)
            except:
                return "Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"
        else:
            return "Błędnie podane ID lub Próba SQL Injection(możesz podac tylko A-Z a-z i 0-9 oraz spacje)"

    def getBook_list(self, rows):
        """Zwraca listę wszystkich ksiazek."""
        try:
            return mysql.get("SELECT * FROM Ksiazka;", rows)
        except:
            return "Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"

    def getBook_sort(self, by_what, order, rows, page):
        """Zwraca posortowana liste ksiazek."""
        """ mysql.check przepuszcza zmienna przez regex'a który sprawdza czy order lub to jak sortujemy przy przekazywaniu zmiennych nie ma w sobie znaków specjalnych  """
        #if mysql.check(order) and mysql.check(by_what):
        try:
            book_list = mysql.get("SELECT * FROM Ksiazka ORDER BY %s %s;" % (by_what, order), rows)
            if page == 0:
                return book_list[0:6]
            else:
                return book_list[page*6:page*6+6]
        except:
            return "getBook_sort: Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"
        #else:
            #return "Błędnie podane ID lub Próba SQL Injection"
            
    def addBook(self, book_id, ilosc):
        try:
            koszyk_id = mysql.get("SELECT idKoszyk FROM Koszyk WHERE status_zamowienia = 0;", 1)
            return mysql.add("INSERT INTO listaKoszyka (idKsiazka, idKoszyk, ilosc) VALUES (%s, %s, %s);" % (book_id, koszyk_id[0][0], ilosc))
        except:
            return "addBook: Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"

    def getBook_price(self):
        try:
            return mysql.get("SELECT ROUND(SUM(cena), 2) FROM Ksiazka where idKsiazka IN (select idKsiazka from listaKoszyka where idKoszyk = (select idKoszyk from Koszyk where idUzytkownik = 1 and status_zamowienia = 0));", 1)
        except:
            return "addBook: Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"

    def getCart_list(self, rows):
        """Zwraca listę wszystkich ksiazek w koszyku."""
        try:
            return mysql.get("SELECT * FROM Ksiazka where idKsiazka IN (select idKsiazka from listaKoszyka where idKoszyk = (select idKoszyk from Koszyk where idUzytkownik = 1  and status_zamowienia = 0));", rows)
        except:
            return "getCart: Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"

    def finalizeOrder(self, user_id):
        """Zaznacza dany koszyk jako zfinalizowany"""
        mysql.add("UPDATE Koszyk SET status_zamowienia = 1 WHERE idUzytkownik = 1 AND status_zamowienia = 0;")
        return mysql.add("INSERT INTO Koszyk (idUzytkownik, data_realizacji) VALUES (1, '9999-12-31 23:59:59');")
        #return "finalizeOrder: Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"
    
    def deleteBook(self, book_id):
        """Usuwa ksiazke z koszyka."""
        try:
            koszyk_id = mysql.get("SELECT idKoszyk FROM Koszyk WHERE status_zamowienia = 0;", 1)
            return mysql.add("DELETE FROM listaKoszyka WHERE idKoszyk=%s AND idKsiazka=%s;" % (koszyk_id[0][0], book_id))
        except:
            return "deleteBook: Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"
        

    def registry(self, login, password, password_2, adres, nr_Telefonu, e_Mail, rows):
        list = [login, password, password_2, adres, nr_Telefonu, e_Mail]
        list_num = ['Login', 'Haslo', 'Haslo ponowne', 'Adres', 'Numer Telefonu', 'E-mail']
        for e, nazwa in zip(list, list_num):
            if e is None:
                return "Pole %s jest puste" % nazwa
        
        if list[1] != list[2]:
            return "Hasla sie roznia"
        for l, nazwa in zip(list, list_num):
            if not check(l):
                return "Podane pole %s jest nieautoryzowane przez serwer" % nazwa


        if (mysql.get("SELECT Count(login) FROM Uzytkownik WHERE login = %s ;", rows) % list[0]) == 1:
            return "Uzytkownik o podanym Loginie jest juz zajety"
    
        cryptedpwd = SHA256.new()
        cryptedpwd.update(list[1])

        mystring = 'INSERT INTO Uzytkownik (login, haslo, adres, nr_telefonu, email) VALUES (\'' + list[0] + '\', \'' + cryptedpwd.hexdigest() + '\', \'' + \
               list[3] + '\', ' + str(list[4]) + '\', \'' + str(list[5]) + '\')'
        mysql.add(mystring)
        Sukces = True
        return Sukces

    def search(self, query, page):
        """ Zwraca wynik wyszukiwania w bazie ksiazek. """
        
        p = re.compile(ur'( [\w]+|^[\w]+)')
        arguments = re.findall(p,query)
        q = re.compile(ur'(-[\w]+)')
        arguments2 = re.findall(q,query)
        
        a  = ''
        z = False
        for x in arguments: #.group(0)
            x = x[1:]
            if z:
                a += ' OR '
            z = True
            a += 'autor like ' + '"%' + x + '%"' ' OR '
            a += 'tytul like ' + '"%' + x + '%"' ' OR '
            a += 'kategoria like ' + '"%' + x + '%" '
        if z and arguments2:
            a += 'AND '
        if arguments2:
            a += 'EXISTS (SELECT * FROM listaTagu LEFT JOIN Tagi ON listaTagu.idTag = Tagi.idTag WHERE Ksiazka.idKsiazka = listaTagu.idKsiazka AND '

        z = False;
        for x in arguments2:
            x = x[1:]
            if z:
                a += ' OR '
            z = True
            a += 'Tagi.nazwaTagu LIKE "%' + x + '%" '

        if z:
            a += ')'    
        a+= ";"
        print 'a = '
        print a
        
        book_list = mysql.get("SELECT * FROM Ksiazka WHERE %s;" % (a), 100)

        if page == 0:
            return book_list[0:6]
        else:
            return book_list[page*6:page*6+6]
            
def main():
    """ Glowna funkcja, uruchamiana przy inicjalizacji PyRo. """
    global mysql

    # Polacz z baza danych
    mysql = database.Database('localhost', 'root', 'root', 'tas')

    # Polacz z PyRo
    library = Library()

    #library.registry('Pindzia', 'qwert123', 'qwert123', 'SerdeczneJP 3', 700880774, 'jezuspan@pieklo.eu', 20)
    Pyro4.Daemon.serveSimple(
            {
                library: "tas.library"
            },
            host = 'localhost',
            port = 8091,
            ns = False)
    

# Uruchamia funkcje glowna.
if __name__=="__main__":
    main()


