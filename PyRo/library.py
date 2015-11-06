# -*- coding: utf-8 -*-

import Pyro4
import database


class Library(object):
    def __init__(self):
        pass

    def test(self):
        return "Test przeszedl pomyslnie."

    def list_contents(self):
        return self.contents

    # def take(self, name, item):
    #     self.contents.remove(item)
    #     print "%s took the %s." % (name, item)

    # def store(self, name, item):
    #     self.contents.append(item)
    #     print "%s stored the %s" % (name, item)


def main():

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


if __name__=="__main__":
    main()

