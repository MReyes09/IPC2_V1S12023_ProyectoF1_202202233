from model.Historial import Historial


class HistorialController:

    def add_Historial(self, listHis, nombre_Pel:str, fechaPel:str, horaPel:str, no_Boletos:int, no_Asientos:int, monto_Total:int):

        lista_Boletos:[] = []

        for i in range(1, no_Boletos + 1):

            codigo_Boleto:str = f"#USACIPC2_202202233_{i}"
            lista_Boletos.append(codigo_Boleto)

        id_Historial = len(listHis) + 1
        nuevo_Historial: Historial = Historial(id_Historial, nombre_Pel, fechaPel, horaPel, monto_Total, no_Asientos, lista_Boletos)
        listHis.append(nuevo_Historial)
        return listHis