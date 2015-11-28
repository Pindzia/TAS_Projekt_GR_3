import Pyro4

class Startup():
    """ Klasa ustanawiajaca polaczenie z PyRo. URI nalezy zmienic na aktualne przy kazdym ponownym polaczeniu. """

    def __init__(self):
        uri = "PYRO:example.library@localhost:39686".strip()
        self.library = Pyro4.Proxy(uri)

pyro = Startup()



