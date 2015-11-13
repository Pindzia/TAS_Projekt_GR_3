# -*- coding: utf-8 -*-

import Pyro4
import database


class Library(object):
    """ Zawiera metody odpytujace baze danych. """

    def __init__(self):
        pass
        # self.contents = []

    def test(self):
        return "Test przeszedl pomyslnie."

    # def list_contents(self):
    #     return self.contents


def main():
    """ Glowna funkcja, uruchamiana przy inicjalizacji PyRo. """

    # Establish database connection
    # mysql = database.database('localhost', 'root', 'root', 'tas')
    # print mysql.get("SELECT tytul FROM Ksiazka WHERE idKsiazka=1;")

    # Establish PyRo connection
    library = Library()
    Pyro4.Daemon.serveSimple(
            {
                library: "example.library"
            },
            ns = False)


# Uruchamia funkcje glowna.
if __name__=="__main__":
    main()

