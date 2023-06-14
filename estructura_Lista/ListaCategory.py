import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from estructura_Lista.ListaPelicula import ListaPelicula
from model.Categoria import Categoria
from model.Pelicula import Pelicula
from node.NodoCategoria import NodoCategory
from node.NodoPelicula import NodoPelicula


class ListaCategory:

    def __init__(self):

        self.cabeza:NodoCategory = None
        self.cola:NodoCategory = None

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

    def update_Categoria(self, nombre:str, opcion:int):

        actual: NodoCategory = self.cabeza

        if actual is None:
            print("No hay categorias")
            return

        if opcion == 1:

            while True:

                categoriaFind = actual.categoria.get_NombreCa()

                if categoriaFind == nombre:

                    print("Actualiza el nombre de la categoria: ")
                    nombre_Nuevo = input("nombre nuevo: ")
                    actual.categoria.set_NombreCa(nombre_Nuevo)
                    break

                elif actual.siguiente == self.cabeza:

                    print("No se encontraron coincidencias \n")
                    break

                else: actual = actual.siguiente

        elif opcion == 2:

            while True:

                categoriaFind = actual.categoria.get_NombreCa()

                if categoriaFind == nombre:

                    print("LLena los siguientes datos para registrar la pelicula\n")
                    titulo: str = input("titulo: ")
                    director: str = input("director: ")
                    anio: int = int(input("año: "))
                    fecha: str = input("fecha: ")
                    hora: str = input("hora: ")
                    cargar_Pelicula: Pelicula = Pelicula(titulo, director, anio, fecha, hora)
                    actual.categoria.get_Peliculas().add_Pelicula(cargar_Pelicula)
                    break

                elif actual.siguiente == self.cabeza:

                    print("No se encontraron coincidencias \n")
                    break

                else: actual = actual.siguiente

        elif opcion == 3:

            while True:

                categoriaFind = actual.categoria.get_NombreCa()

                if categoriaFind == nombre:

                    titulo:str = input("titulo de la pelicula a actualizar\n"
                                       "tu respuesta: ")
                    actual.categoria.get_Peliculas().actualizar_Pelicula(titulo)
                    break

                elif actual.siguiente == self.cabeza:

                    print("No se encontraron coincidencias \n")
                    break

                else:
                    actual = actual.siguiente

        elif opcion == 4:

            while True:

                categoriaFind = actual.categoria.get_NombreCa()

                if categoriaFind == nombre:

                    titulo: str = input("titulo de la pelicula a eliminar\n"
                                        "tu respuesta: ")
                    actual.categoria.get_Peliculas().eliminar_Pelicula(titulo)
                    break

                elif actual.siguiente == self.cabeza:

                    print("No se encontraron coincidencias \n")
                    break

                else:
                    actual = actual.siguiente


    def delete_Categoria(self, nombre:str):

        if self.cabeza is None:
            print("La lista de categorias esta vacia!")
            return  # Lista vacía, no se puede eliminar

        nodo_actual = self.cabeza

        while True:
            if nodo_actual.categoria.get_NombreCa() == nombre:
                nodo_anterior = nodo_actual.anterior
                nodo_siguiente = nodo_actual.siguiente

                if nodo_actual == self.cabeza:
                    self.cabeza = nodo_siguiente
                if nodo_actual == self.cola:
                    self.cola = nodo_anterior

                if nodo_anterior is not None:
                    nodo_anterior.siguiente = nodo_siguiente
                if nodo_siguiente is not None:
                    nodo_siguiente.anterior = nodo_anterior

                if self.cabeza is None and self.cola is None:
                    # Lista vacía después de eliminar el nodo
                    break

                if nodo_actual == self.cabeza:
                    self.cabeza = nodo_siguiente
                print("Se encontro y elimino la categoria")
                break  # Se encontró y eliminó el nodo
            nodo_actual = nodo_actual.siguiente

            if nodo_actual == self.cabeza:
                print("no se encontraron coincidencias en el nombre")
                break  # Se recorrió toda la lista sin encontrar el nodo

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
                if actual.categoria.get_Peliculas() is not None:
                    categoria_Pelis.Listar_Peliculas(actual.categoria.get_Peliculas())
                    print(" ")
                else: print("Esta categoria no tiene peliculas aun")
                actual = actual.siguiente

            elif opcion == 2:

                if actual.categoria.get_Peliculas() is not None:
                    categoria_Pelis.Listar_Peliculas(actual.categoria.get_Peliculas())
                    print(" ")
                actual = actual.siguiente

            elif opcion == 3:

                print(f"Categoria: {actual.categoria.get_NombreCa()}")
                actual = actual.siguiente

            else:

                print("Esta opcion es incorrecta\n")
                break

            if actual == self.cabeza:
                break

    def CargarXML_Category(self):

        self.cabeza = None
        with open('categorias_peliculas.xml', 'r', encoding='utf-8') as archivo:
            tree = ET.parse(archivo)
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

    def actualiar_XML(self):
        root = ET.Element("categorias")

        actual = self.cabeza

        while actual is not None:
            categoria = actual.categoria
            nueva_categoria = ET.SubElement(root, "categoria")

            nombre = ET.SubElement(nueva_categoria, "nombre")
            nombre.text = categoria.get_NombreCa()

            peliculas = ET.SubElement(nueva_categoria, "peliculas")

            if categoria.get_Peliculas() is not None:
                lista_peliculas = categoria.get_Peliculas()

                nodo_actual:NodoPelicula = lista_peliculas.cabeza

                while nodo_actual is not None:
                    pelicula = nodo_actual.pelicula
                    nueva_pelicula = ET.SubElement(peliculas, "pelicula")

                    titulo = ET.SubElement(nueva_pelicula, "titulo")
                    titulo.text = pelicula.get_titulo()

                    director = ET.SubElement(nueva_pelicula, "director")
                    director.text = pelicula.get_director()

                    anio = ET.SubElement(nueva_pelicula, "anio")
                    anio.text = str(pelicula.get_anio())

                    fecha = ET.SubElement(nueva_pelicula, "fecha")
                    fecha.text = pelicula.get_fecha()

                    hora = ET.SubElement(nueva_pelicula, "hora")
                    hora.text = pelicula.get_hora()

                    if nodo_actual.siguiente == lista_peliculas.cabeza:
                        break
                    else: nodo_actual = nodo_actual.siguiente

            if actual.siguiente == self.cabeza:
                break
            else: actual = actual.siguiente

        xml_str = ET.tostring(root, encoding="utf-8")
        dom = minidom.parseString(xml_str)
        with open("categorias_peliculas.xml", "w") as archivo:
            archivo.write(dom.toprettyxml(indent="   "))
        print("\nSe ha actualizado el archivo XML de categorías exitosamente.")