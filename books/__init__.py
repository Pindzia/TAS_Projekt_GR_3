import Pyro4

class Startup():
    """ Klasa ustanawiajaca polaczenie z PyRo. """

    def __init__(self):
        self.ev = 'VAR'
        uri = "PYRO:example.library@localhost:43659".strip()
        self.library = Pyro4.Proxy(uri)


pyro = Startup()