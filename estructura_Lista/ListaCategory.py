import xml.etree.ElementTree as ET

from estructura_Lista.ListaPelicula import ListaPelicula
from model.Categoria import Categoria
from model.Pelicula import Pelicula
from node.NodoCategoria import NodoCategory


class ListaCategory:

    def __init__(self):

        self.cabeza = None
        self.cola = None

    def add_Categoria(self, categoria: Categoria):

        nuevo_Nodo = NodoCategory(categoria)

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

    def categoria_Buscar_Peli(self, titulo:str):

        actual: NodoCategory = self.cabeza

        if actual is None:
            print("No hay categorias")
            return

        while True:

            buscarPelis = ListaPelicula()
            categoria_Pelis = actual.categoria.get_Peliculas()
            finded_Pelicula = buscarPelis.buscar_Pelicula(categoria_Pelis, titulo)

            if finded_Pelicula == None:
                if actual.siguiente == self.cabeza:
                    print("No se encontraron coincidencias")
                    break
                else:
                    actual = actual.siguiente
            else:
                return finded_Pelicula

    def Listar_Categorias(self, opcion: int) -> None:

        actual: NodoCategory = self.cabeza

        if actual is None:
            print("No hay categorias")
            return

        while True:

            categoria_Pelis: ListaPelicula = ListaPelicula()

            if opcion == 1:

                print(f"Categoria: {actual.categoria.get_NombreCa()}")
                categoria_Pelis.Listar_Peliculas(actual.categoria.get_Peliculas())
                print(" ")
                actual = actual.siguiente

            elif opcion == 2:

                categoria_Pelis.Listar_Peliculas(actual.categoria.get_Peliculas())
                print(" ")
                actual = actual.siguiente

            else:

                print("Esta opcion es incorrecta\n")
                break

            if actual == self.cabeza:
                break

    def CargarXML_Category(self):

        tree = ET.parse('categorias_peliculas.xml')
        root = tree.getroot()

        for categoria in root.findall('categoria'):

            lista_Pelicula: ListaPelicula = ListaPelicula()
            nombre: str = categoria.find('nombre').text

            for pelicula in categoria.findall("peliculas/pelicula"):

                titulo: str = pelicula.find('titulo').text
                director: str = pelicula.find('director').text
                anio: int = int(pelicula.find('anio').text)
                fecha: str = pelicula.find('fecha').text
                hora: str = pelicula.find('hora').text
                cargar_Pelicula: Pelicula = Pelicula(titulo, director, anio, fecha, hora)
                lista_Pelicula.add_Pelicula(cargar_Pelicula)

            cargar_Categoria: Categoria = Categoria(nombre, lista_Pelicula)
            self.add_Categoria(cargar_Categoria)
