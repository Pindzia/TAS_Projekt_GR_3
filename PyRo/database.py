#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys

class Database():
    """ Obsluguje polaczenie oraz zapytania do bazy danych. """

    def __init__(self, host, user, password, base):
        """ Laczy z baza danych. """
        global con

        try:
            con = _mysql.connect(host, user, password, base)
            
            print "Polaczono z baza danych."
        
        except _mysql.Error, e:
          
            print "Blad %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

    def get(self, question, rows):
        """ Odpytuje baze danych. Drugim argumentem jest liczba wpisow, ktora chcemy uzyskac."""

        con.query(question)
        result = con.use_result()
        return result.fetch_row(rows)

    def add(self, question):
        """ Modyfikuje baze danych. """
        con.query(question)