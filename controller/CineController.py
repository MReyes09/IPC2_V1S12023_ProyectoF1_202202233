import xml.etree.ElementTree as ET

from estructura_Lista.ListaSala import ListaSala
from model.Cine import Cine
from model.Sala import Sala


class CineController:

    def CargarXML_Cine(self, listaCines: []):

        tree = ET.parse('salas.xml')
        root = tree.getroot()

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

        for cine in listaCines:

            print(f"Cine: {cine.get_nombre()}")
            lista_Salas: ListaSala = cine.get_salas()
            lista_Salas.listar_Salas()

    def buscar_Sala_In_Cine(self, numero_Sala:str, numero_Asientos:int, listaCines:[]):

        for cine in listaCines:

            lista_Salas: ListaSala = cine.get_salas()
            validar_Sala = lista_Salas.buscar_Sala(numero_Sala, numero_Asientos)
            return  validar_Sala