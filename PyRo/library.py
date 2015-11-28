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
            return mysql.get("SELECT idKsiazka, tytul, autor, cena, dict_img, kategoria FROM Ksiazka WHERE idKsiazka=%s;" % (id))
        except:
            return "Najprawdopodobniej podales zle ID ksiazki lub wystapil blad w library.py"


def main():
    """ Glowna funkcja, uruchamiana przy inicjalizacji PyRo. """

    global mysql

    # Polacz z baza danych
    mysql = database.Database('localhost', 'root', 'root', 'tas')

    # Polacz z PyRo
    library = Library()
    Pyro4.Daemon.serveSimple(
            {
                library: "example.library"
            },
            ns = False)


# Uruchamia funkcje glowna.
if __name__=="__main__":
    main()


