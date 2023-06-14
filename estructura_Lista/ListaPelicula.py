from model.Pelicula import Pelicula
from node.NodoPelicula import NodoPelicula


class ListaPelicula:

    def __init__(self):

        self.cabeza: NodoPelicula = None
        self.cola: NodoPelicula = None

    def add_Pelicula(self, pelicula: Pelicula):

        nuevo_Nodo: NodoPelicula = NodoPelicula(pelicula)

        if self.cabeza is None:

            self.cabeza = nuevo_Nodo
            self.cola = nuevo_Nodo
            nuevo_Nodo.anterior = nuevo_Nodo
            nuevo_Nodo.siguiente = nuevo_Nodo

        else:

            nuevo_Nodo.anterior = self.cola
            nuevo_Nodo.siguiente = self.cabeza
            self.cola.siguiente = nuevo_Nodo
            self.cabeza.anterior = nuevo_Nodo
            self.cola = nuevo_Nodo

    def Listar_Peliculas(self, listaDePelis):

        actual: NodoPelicula = listaDePelis.cabeza

        if actual is None:
            print("No hay peliculas")
            return

        while True:

            print(f"Titulo: {actual.pelicula.get_titulo()} \n"
                  f"director: {actual.pelicula.get_director()}\n"
                  f"anio: {actual.pelicula.get_anio()}\n"
                  f"fecha: {actual.pelicula.get_fecha()}\n"
                  f"hora: {actual.pelicula.get_hora()}\n")

            if listaDePelis.cabeza == actual.siguiente:

                break

            else:
                actual = actual.siguiente

    def buscar_Pelicula(self, listaDePelis, titulo):

        actual: NodoPelicula = listaDePelis.cabeza

        if actual is None:
            print("No hay peliculas")
            return
        finded_Pelicula:Pelicula

        while True:

            getPelicula:Pelicula = actual.pelicula

            if getPelicula.get_titulo() == titulo:

                finded_Pelicula = getPelicula
                return finded_Pelicula

            elif listaDePelis.cabeza == actual.siguiente:
                return None
            else:
                actual = actual.siguiente

    def actualizar_Pelicula(self, titulo:str):

        actual: NodoPelicula = self.cabeza

        if actual is None:
            print("No hay peliculas")
            return
        finded_Pelicula: Pelicula

        while True:

            getPelicula: Pelicula = actual.pelicula

            if getPelicula.get_titulo() == titulo:

                print("\n Cambia solo la información que deseas editar, sino copia y pega lo del parentesis")
                pelicula_Ac: Pelicula = actual.pelicula
                pelicula_Ac.set_titulo(input(f"titulo ({pelicula_Ac.get_titulo()}): "))
                pelicula_Ac.set_director(input(f"director ({pelicula_Ac.get_director()}): "))
                pelicula_Ac.set_anio(int(input(f"año ({pelicula_Ac.get_anio()}): ")))
                pelicula_Ac.set_fecha(input(f"fecha ({pelicula_Ac.get_fecha()}): "))
                pelicula_Ac.set_hora(input(f"hora ({pelicula_Ac.get_hora()}): "))
                actual.pelicula = pelicula_Ac
                while True:
                    if actual.siguiente == self.cabeza:
                        return actual
                    else:
                        actual = actual.siguiente

            elif self.cabeza == actual.siguiente:
                return None
            else:
                actual = actual.siguiente

    def eliminar_Pelicula(self, titulo:str):

        if self.cabeza is None:
            print("No hay películas en la lista.")
            return

        actual = self.cabeza

        while True:
            if actual.pelicula.get_titulo() == titulo:
                if actual == self.cabeza:
                    # Caso especial: el nodo a eliminar es el nodo cabeza
                    if actual == actual.siguiente:
                        # Caso especial: solo hay un nodo en la lista
                        self.cabeza = None
                        self.cola = None
                    else:
                        self.cabeza = actual.siguiente
                        self.cola.siguiente = self.cabeza
                        self.cabeza.anterior = self.cola
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return

            actual = actual.siguiente

            if actual == self.cabeza:
                break

        print("No se encontró la película en la lista.")
