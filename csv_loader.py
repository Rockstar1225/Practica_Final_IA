""" Módulo para representar los objetos tabla en formato csv."""
import csv
import io
import os


class CSVloader:
    """Clase que representa la tabla de probabilidades condicionadas dado un archivo csv."""
    def __init__(self, estados: list):
        self.contenido = []
        self.indices = estados

    def load_csv(self, path: str):
        """Funcion que carga la tabla en el contenido de la clase."""
        file = open(os.getcwd() + path, encoding='utf-8')
        reader = csv.reader(file)
        for row in reader:
            self.contenido.append(row)
        file.close()

    def localizar_probabilidad(self, estado_inicial: float, estado_final: float) -> int:
        """Localizar un elemento en el contenido del csv cargado"""

        if not self.contenido:
            raise ValueError("El contenido del csv no está cargado!!!")

        if estado_inicial not in self.indices or estado_final not in self.indices:
            raise ValueError("Los estados de localización no son los correctos!!!")

        return int(self.contenido[self.indices.index(estado_inicial)][self.indices.index(estado_final)])
