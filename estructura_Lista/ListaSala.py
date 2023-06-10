from model.Sala import Sala
from node.NodoSala import NodoSala


class ListaSala:

    def __init__(self):
        self.cabeza: NodoSala = None

    def add_Sala(self, sala: Sala):

        new_nodo = NodoSala(sala)

        if self.cabeza is None:

            self.cabeza = new_nodo

        else:

            actual: NodoSala = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = new_nodo

    def listar_Salas(self):

        if self.cabeza is None:

            print("No tiene salas")

        else:

            nodoSala: NodoSala = self.cabeza

            while nodoSala is not None:

                sala = nodoSala.sala
                print(f"    numero: {sala.get_numero()}\n"
                      f"    asientos: {sala.get_asientos()}\n")
                nodoSala = nodoSala.siguiente