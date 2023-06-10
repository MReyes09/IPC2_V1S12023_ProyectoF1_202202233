
class Historial:

    def __init__(self, id_Historial:int, nombre_Pel:str, fecha_P:str, hora:str,  monto_Tota: int, no_Asientos:int, numero_Boleto = None):
        self.id_Historial = id_Historial
        self.nombre_Pel = nombre_Pel
        self.fecha_P = fecha_P
        self.hora = hora
        self.monto_Tota = monto_Tota
        self.numero_Boleto = numero_Boleto if numero_Boleto is not None else []
        self.asientos = no_Asientos

    def set_no_Asientos(self, no_Asientos):
        self.asientos = no_Asientos

    def get_No_Asientos(self):
        return self.asientos

    def get_id_Historial(self) -> int:
        return self._id_Historial

    def set_id_Historial(self, id_Historial: int):
        self._id_Historial = id_Historial

    def get_nombre_Pel(self) -> str:
        return self._nombre_Pel

    def set_nombre_Pel(self, nombre_Pel: str):
        self._nombre_Pel = nombre_Pel

    def get_fecha_P(self) -> str:
        return self._fecha_P

    def set_fecha_P(self, fecha_P: str):
        self._fecha_P = fecha_P

    def get_hora(self) -> str:
        return self._hora

    def set_hora(self, hora: str):
        self._hora = hora

    def get_monto_Tota(self) -> int:
        return self._monto_Tota

    def set_monto_Tota(self, monto_Tota: int):
        self._monto_Tota = monto_Tota

    def get_numero_Boleto(self):
        return self._numero_Boleto

    def set_numero_Boleto(self, numero_Boleto):
        self._numero_Boleto = numero_Boleto