from model.Categoria import Categoria


class NodoCategory:

    def __init__(self, categoria: Categoria):

        self.categoria = categoria
        self.anterior = None
        self.siguiente = None