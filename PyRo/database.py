#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys

class database():

    def __init__(self, host, user, password, base):
        """ Connect to database """
        global con

        try:
            con = _mysql.connect(host, user, password, base)
            
            print "Database connected."
        
        except _mysql.Error, e:
          
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

    def get(self, question):
        """Return database query."""

        con.query(question)
        result = con.use_result()
        return result.fetch_row()[0]

    def add(self, question):
        """Adds query to database."""
        con.query(question)