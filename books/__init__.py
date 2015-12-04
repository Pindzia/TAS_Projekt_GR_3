import Pyro4
from TAS.settings import PYRO_URI

class Startup():
    """ Klasa ustanawiajaca polaczenie z PyRo. URI nalezy zmienic na aktualne przy kazdym ponownym polaczeniu. """

    def __init__(self):
        uri = PYRO_URI.strip()
        self.library = Pyro4.Proxy(uri)

pyro = Startup()



