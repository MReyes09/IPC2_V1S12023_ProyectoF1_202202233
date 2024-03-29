from model.Historial import Historial


class HistorialController:

    def add_Historial(self, listHis, nombre_Pel:str, fechaPel:str, horaPel:str, no_Boletos:int, no_Asientos:int, monto_Total:int, incremental_Boletos:int):

        lista_Boletos:[] = []
        sumar_boleto:int = incremental_Boletos

        for i in range(1, no_Boletos + 1):
            sumar_boleto += 1
            codigo_Boleto:str = f"#USACIPC2_202202233_{sumar_boleto}"
            lista_Boletos.append(codigo_Boleto)

        id_Historial = len(listHis) + 1
        nuevo_Historial: Historial = Historial(id_Historial, nombre_Pel, fechaPel, horaPel, monto_Total, no_Asientos, lista_Boletos)
        listHis.append(nuevo_Historial)
        return listHis

    def listar_Historial(self, listHis):

        if len(listHis) == 0:

            print("Aún no has comprado boletos")

        else:

            for historial in listHis:

                print(f"id_Historial: {historial.get_id_Historial()}\n"
                      f"    pelicula: {historial.get_nombre_Pel()}\n"
                      f"    fecha: {historial.get_fecha_P()}\n"
                      f"    hora: {historial.get_hora()}\n"
                      f"    Boletos: [")
                list_Boletos = historial.get_numero_Boleto()

                for boletos in list_Boletos:

                    print(f"        {boletos}")

                print(f"    ]")
                print(f"    numero de asientos: {historial.get_No_Asientos()}\n"
                      f"    monto total: {historial.get_monto_Tota()}\n \n")