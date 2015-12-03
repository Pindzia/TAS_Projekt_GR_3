# -*- coding: utf-8 -*-

import Pyro4
import database


class Library(object):
    """ Zawiera metody odpytujace baze danych. """

    def __init__(self):
        pass

    def test(self):
        return "Test przeszedl pomyslnie."

    def getBook_id(self, id):
        """ Zwraca ksiazke z podanym id. """

        try:
            return mysql.get("SELECT idKsiazka, tytul, autor, cena, dict_img, kategoria FROM Ksiazka WHERE idKsiazka=%s;" % (id), 1)
        except:
            return "Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"

    def getBook_list(self, rows):
        "Zwraca listę wszystkich ksiazek."

        return mysql.get("SELECT * FROM Ksiazka;", rows)


    def getBook_sort(self, by_what, order, rows):
        "Zwraca posortowana liste ksiazek."

        return mysql.get("SELECT * FROM Ksiazka ORDER BY %s %s;" % (by_what, order), rows)


def main():
    """ Glowna funkcja, uruchamiana przy inicjalizacji PyRo. """

    global mysql

    # Polacz z baza danych
    mysql = database.Database('localhost', 'root', 'root', 'tas')

    # Polacz z PyRo
    library = Library()
    Pyro4.Daemon.serveSimple(
            {
                library: "tas.library"
            },
            host = 'localhost',
            port = 8090,
            ns = False)


# Uruchamia funkcje glowna.
if __name__=="__main__":
    main()


