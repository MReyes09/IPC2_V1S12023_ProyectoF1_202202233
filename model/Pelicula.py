
class Pelicula:

    def __init__(self, titulo: str, director: str, anio: int, fecha: str, hora: str):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora

    def get_titulo(self) -> str:
        return self.titulo

    def set_titulo(self, nuevo_titulo: str):
        self.titulo = nuevo_titulo

    def get_director(self) -> str:
        return self.director

    def set_director(self, nuevo_director: str):
        self.director = nuevo_director

    def get_anio(self) -> int:
        return self.anio

    def set_anio(self, nuevo_anio: int):
        self.anio = nuevo_anio

    def get_fecha(self) -> str:
        return self.fecha

    def set_fecha(self, nueva_fecha: str):
        self.fecha = nueva_fecha

    def get_hora(self) -> str:
        return self.hora

    def set_hora(self, nueva_hora: str):
        self.hora = nueva_hora
