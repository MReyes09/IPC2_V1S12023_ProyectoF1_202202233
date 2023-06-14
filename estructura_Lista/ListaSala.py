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

    def buscar_Sala(self, numero_Sala: str, numero_Asientos: int, opcion:int):

        if self.cabeza is None:

            print("No tiene salas")
            return

        else:

            nodoSala: NodoSala = self.cabeza

            while nodoSala is not None:

                sala = nodoSala.sala

                if opcion == 1:
                    if sala.get_numero() == numero_Sala and sala.get_asientos() >= numero_Asientos:

                        return True

                    else:
                        nodoSala = nodoSala.siguiente

                elif opcion == 2: #Actualizar sala con coincidencia

                    if sala.get_numero() == numero_Sala:

                        print("Escribe lo que se te pide o copia y pega el contenido del parentesis")
                        sala.set_numero(input(f"numero ({sala.get_numero()}): "))
                        sala.set_asientos(int(input(f"No. asientos ({sala.get_asientos()}): ")))
                        nodoSala.sala = sala
                        return

                    else: nodoSala = nodoSala.siguiente

            print("Verifica que el numero de sala o numero de asientos")
            return False

    def eliminar_Sala(self, numero_Sala: str):

        if self.cabeza is None:
            return

            # Caso 1: El nodo a eliminar es el primero
        if self.cabeza.sala.get_numero() == numero_Sala:
            siguiente_nodo = self.cabeza.siguiente
            if siguiente_nodo is not None:
                siguiente_nodo.anterior = None
            self.cabeza = siguiente_nodo
            return

        nodo_actual:NodoSala = self.cabeza
        # Caso 2: El nodo a eliminar está en medio
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.sala.get_numero() == numero_Sala:
                nodo_siguiente = nodo_actual.siguiente.siguiente
                nodo_actual.siguiente = nodo_siguiente
                if nodo_siguiente is not None:
                    nodo_siguiente.anterior = nodo_actual
                return
            nodo_actual = nodo_actual.siguiente

        # Caso 3: El nodo a eliminar es el último
        if nodo_actual.sala.get_numero() == numero_Sala:
            nodo_anterior = nodo_actual.anterior
            if nodo_anterior is not None:
                nodo_anterior.siguiente = None
            return

        # Si el dato no se encuentra en la lista, se puede mostrar un mensaje o realizar otra acción
        print("El dato no existe en la lista.")