# -*- coding: utf-8 -*-

import Pyro4
import database
import crypto
import re


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

    def getBook_sort(self, by_what, order, rows):
        """Zwraca posortowana liste ksiazek."""
        """ mysql.check przepuszcza zmienna przez regex'a który sprawdza czy order lub to jak sortujemy przy przekazywaniu zmiennych nie ma w sobie znaków specjalnych  """
        if mysql.check(order) and mysql.check(by_what):
            try:
                return mysql.get("SELECT * FROM Ksiazka ORDER BY %s %s;" % (by_what, order), rows)
            except:
                return "Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"
        else:
            return "Błędnie podane ID lub Próba SQL Injection"
            
    def addBook(self,book_id,ilosc,koszyk_id="1"):
        try:
            return mysql.add("INSERT INTO listaKoszyka (idKsiazek, idKoszyka, ilość) VALUES (%s %s %s);" % (book_id, koszyk_id, ilosc))
        except:
            return "Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"
        

    def registry(self , login, password, password_2, adres, nr_Telefonu, rows):
        list = [login, password, password_2, adres, nr_Telefonu]
        list_num = ['Login', 'Hasło', 'Hasło ponowne', 'Adres', 'Numer Telefonu']
        """sprawdzanie czy pola są puste """
        for e, nazwa in zip(list, list_num):
            if e is None:
                return "Pole %s jest puste" % nazwa
                
        """sprawdzenie czy hasło nr 1 zgadza sie z nr 2"""
        if password != password_2:
            return "Hasło pierwsze różni się od hasła drugiego"
            
        """sprawdzanie danych wprowadzanych w celu określenia ich poprawności"""
        for l, nazwa in zip(list, list_num):
            if not mysql.check(l):
                return "Podane pole %s jest niepoprawnie wprowadzone" % nazwa
        
        """sprawdzamy czy sa uzytkownicy o tym loginie"""
        if (mysql.get("SELECT Count(login) FROM Uzytkownik WHERE login = "+list[0]+" ;", rows)) == 1:
            return "Użytkownik o podanym Loginie już istnieje"
        
        """przy wprowadzaniu danych nie popełniliśmy błędu zatem rejestrujemy"""
        
        """zahashowanie hasła"""
        cryptedpwd = SHA512.new()
        cryptedpwd.update(list[1])
        
        """REJESTRACJA czyli dodanie rekordu"""
        mysql.add("INSERT INTO Uzytkownik (login, haslo, adres, nr_telefonu) VALUES (\'"+list[0]+"\', \'"+cryptedpwd+"\', \'"+list[3]+"\', \'"+str(list[4])+"\')")
        
        return "Gratulujemy Pomyślnej Rejestracji"

    def search(self, query):
        p = re.compile(ur'([\w]+)')
        arguments = re.findall(p,query)
        
        a  = ''
        z = False
        for x in arguments: #.group(0)
            if z:
                a += ' OR '
            z = True
            a += "'" + x + "'" + 'IN (autor, tytul, kategoria)'
        a+= ";"
        return mysql.get("SELECT * FROM Ksiazka WHERE %s;" % (a), 20)
            
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


