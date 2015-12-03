import Pyro4

class Startup():
    """ Klasa ustanawiajaca polaczenie z PyRo. URI nalezy zmienic na aktualne przy kazdym ponownym polaczeniu. """

    def __init__(self):
        uri = "PYRO:tas.library@localhost:8090".strip()
        self.library = Pyro4.Proxy(uri)

pyro = Startup()



