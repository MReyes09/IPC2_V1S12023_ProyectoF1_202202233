from model.Sala import Sala


class NodoSala:
    
    def __init__(self, sala: Sala):

        self.sala = sala
        self.anterior = None
        self.siguiente = None