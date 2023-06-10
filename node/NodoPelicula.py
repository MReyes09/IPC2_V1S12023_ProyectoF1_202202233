from model.Pelicula import Pelicula


class NodoPelicula:

    def __init__(self, pelicula: Pelicula):

        self.pelicula = pelicula
        self.anterior = None
        self.siguiente = None