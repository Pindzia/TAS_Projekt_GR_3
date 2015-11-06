import sys
import Pyro4

uri = input("Enter the uri of the library: ").strip()
library = Pyro4.Proxy(uri)
print library.test()
