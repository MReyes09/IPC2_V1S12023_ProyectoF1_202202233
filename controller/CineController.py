import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from estructura_Lista.ListaSala import ListaSala
from model.Cine import Cine
from model.Sala import Sala
from node.NodoSala import NodoSala


class CineController:

    def CargarXML_Cine(self, listaCines: []):

        tree = ET.parse('salas.xml')
        root = tree.getroot()

        listaCines.clear()

        for cine in root.findall('cine'):

            lista_Sala: ListaSala = ListaSala()
            nombre_Cine: str = cine.find('nombre').text

            for sala in cine.findall('salas/sala'):

                numero:str = sala.find('numero').text
                asientos:int = int(sala.find('asientos').text)
                cargar_Sala: Sala = Sala(numero, asientos)
                lista_Sala.add_Sala(cargar_Sala)

            cargar_Cine: Cine = Cine(nombre_Cine, lista_Sala)
            listaCines.append(cargar_Cine)

        return listaCines

    def Listar_Cines_Salas(self, listaCines:[]):

        if len(listaCines) != 0:
            for cine in listaCines:

                print(f"Cine: {cine.get_nombre()}")
                if cine.get_salas() is not None:
                    print("  [")
                    lista_Salas: ListaSala = cine.get_salas()
                    lista_Salas.listar_Salas()
                    print("  ]")
                else: print("Aun no se le agregan Salas\n")
        else:print("La lista de cines esta vacia!!\n")

    def buscar_Sala_In_Cine(self, numero_Sala:str, numero_Asientos:int, listaCines:[]):

        for cine in listaCines:

            lista_Salas: ListaSala = cine.get_salas()
            validar_Sala = lista_Salas.buscar_Sala(numero_Sala, numero_Asientos, 1)
            return  validar_Sala

    def agregar_Cine(self, listaCines, nombre:str) -> []:

        agregar_Cine: Cine = Cine(nombre)
        listaCines.append(agregar_Cine)

        return listaCines

    def modificar_Cine(self, listaCines, nombre: str, opcion:int) -> []:

        indice: int = 0
        for cine in listaCines:

            if cine.get_nombre() == nombre:

                if opcion == 1:
                    nombre_Nuevo:str = input("Actualizar el nombre de cine\n"
                                             "nombre: ")
                    if cine.get_salas() is not None:

                        up_Cine: Cine = Cine(nombre_Nuevo, cine.get_salas())
                        listaCines[indice] = up_Cine
                        return listaCines

                    else:

                        up_Cine: Cine = Cine(nombre_Nuevo)
                        listaCines[indice] = up_Cine
                        return listaCines

                elif opcion == 2:

                    print("Para crear una nueva sala, llena los siguientes datos\n ")
                    numero:str = "#USACIPC2_202202233_" + input("Escibe el numero de sala #USACIPC2_202202233_Numero: ")
                    asientos:int = int(input("numero de asientos: "))

                    sala_Nueva: Sala = Sala(numero, asientos)
                    if cine.get_salas() is None:

                        lista_Nueva: ListaSala = ListaSala()
                        lista_Nueva.add_Sala(sala_Nueva)
                        cine.set_salas(lista_Nueva)

                    else:

                        cine.get_salas().add_Sala(sala_Nueva)

                    listaCines[indice] = cine
                    print("Se agrego la sala correctamente")
                    return listaCines

                elif opcion == 3:

                    print("escribe el numero de sala que deseas modificar")
                    numero_Sala:str = input("Numero de sala:")
                    cine.get_salas().buscar_Sala(numero_Sala, 0, 2)
                    listaCines[indice] = cine
                    print("\n SE ACTUALIZO LA SALA CON EXITO")
                    return listaCines

                elif opcion == 4:

                    print("escribe el numero de sala que deseas eliminar")
                    numero_Sala: str = input("Numero de sala:")
                    cine.get_salas().eliminar_Sala(numero_Sala)
                    listaCines[indice] = cine
                    print("\n SE ELIMINO LA SALA CON EXITO")
                    return listaCines

            else: indice += 1

        print("No se encontro ninguna coincidencia con el nombre")

    def eliminar_Cine(self, listaCines, nombre:str) -> []:

        indice: int = 0

        for cine in listaCines:

            if cine.get_nombre() == nombre:

                del listaCines[indice]
                print(f"se elimino con exito el cine {nombre}\n")
                return listaCines

            else: indice += 1
        print(f"No se encontro ningun cine con nombre {nombre}\n")

    def actualizar_XML(self, listaCines):

        root = ET.Element("cines")

        if len(listaCines) !=0:

            for cine in listaCines:

                nuevo_Cine = ET.SubElement(root, "cine")
                nombre = ET.SubElement(nuevo_Cine, "nombre")
                nombre.text = cine.get_nombre()

                salas = ET.SubElement(nuevo_Cine, "salas")

                if cine.get_salas() is not None:
                    lista_Salas:ListaSala = cine.get_salas()
                    nodo_actual: NodoSala = lista_Salas.cabeza

                    while nodo_actual is not None:

                        getSala = nodo_actual.sala
                        nueva_Sala = ET.SubElement(salas, "sala")

                        numero = ET.SubElement(nueva_Sala, "numero")
                        numero.text = getSala.get_numero()

                        asientos = ET.SubElement(nueva_Sala, "asientos")
                        asientos.text = str(getSala.get_asientos())

                        nodo_actual = nodo_actual.siguiente

            xml_str = ET.tostring(root, encoding="utf-8")
            dom = minidom.parseString(xml_str)
            with open("salas.xml", "w") as archivo:
                archivo.write(dom.toprettyxml(indent="   "))
            print("\nSe ha actualizado el archivo XML de Cines exitosamente.")