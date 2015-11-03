# This is the code that visits the warehouse.
import sys
import Pyro4
from person import Person

uri = input("Enter the uri of the warehouse: ").strip()
warehouse = Pyro4.Proxy(uri)
janet = Person("Janet")
henry = Person("Henry")
janet.visit(warehouse)
henry.visit(warehouse)