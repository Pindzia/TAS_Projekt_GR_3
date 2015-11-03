# -*- coding: utf-8 -*-

import Pyro4
import person
import database


class Warehouse(object):
    def __init__(self):
        self.contents = ["chair", "bike", "flashlight", "laptop", "couch"]

    def list_contents(self):
        return self.contents

    def take(self, name, item):
        self.contents.remove(item)
        print "%s took the %s." % (name, item)

    def store(self, name, item):
        self.contents.append(item)
        print "%s stored the %s" % (name, item)


def main():

    mysql = database.database('localhost', 'root', 'root', 'tas')
    print mysql.get("SELECT tytul FROM Ksiazka WHERE idKsiazka=1;")

    # Establish PyRo connection
    warehouse = Warehouse()
    Pyro4.Daemon.serveSimple(
            {
                warehouse: "example.warehouse"
            },
            ns = False)


if __name__=="__main__":
    main()

