# -*- coding: utf-8 -*-

import Pyro4
import database


class Library(object):
    """ Zawiera metody odpytujace baze danych. """

    def __init__(self):
        pass

    def test(self):
        return "Test przeszedl pomyslnie."

    def get_book(self, id):
        """ Przykladowa funkcja z zapytaniem do bazy. """
        # book = mysql.get("SELECT tytul FROM Ksiazka WHERE idKsiazka=%s;") % (id)



def main():
    """ Glowna funkcja, uruchamiana przy inicjalizacji PyRo. """

    # Establish database connection
    # mysql = database.database('localhost', 'root', 'root', 'tas')

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

