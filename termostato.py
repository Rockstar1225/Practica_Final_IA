"""
    Este es el módulo que representa el termostato y su comportamiento en la práctica.
"""
import random


class Termostato:
    """ Clase que representa el objeto termostato y su funcionamiento."""

    def __init__(self, input_temperatura: int, acciones: list, costes: list):
        self.temp_usuario = input_temperatura
        self.acciones = acciones
        self.costes = costes
        self.temp_real = random.randint(16, 25)
        self.probabilidades = {}

        if self.comprobar_parametros():
            self.inicializar_probabilidades()
        else:
            raise ValueError("Parámetros de instancia no correctos !!!")

    def inicializar_probabilidades(self) -> None:
        """
            Esta función prepara el diccionario para almacenar las probabilidades.
            Éstas se almacenarán de esta manera:

                - En el diccionario principal habrá una entrada para cada acción a realizar.

                - Como valores de las acciones a realizar, habrá un subdiccionario
                    para cada uno de los estados posibles.

                - Para definir las probabilidades de las acciones
                    teniendo en cuenta el estado actual y la acción a realizar,
                    se accederá a el diccionario de la siguiente manera:
                        self.probabilidades[acción][estado].

                - La consulta anteríor retornará los valores de subir un grado/medio
                    o bajar un grado/medio.

                - Para la localización de dichos valores en la lista anterior,
                    se organizará de la siguiente manera:
                        + Subir medio grado la temperatura: indice 0.
                        + Subir un grado la temperatura: indice 1.
                        + Bajar medio grado la temperatura: indice 2.
                        + Bajar un grado la temperatura: indice 3.

                - Ejemplo:
                    Con la consulta "self.probabilidades["encender"][18][0]" se estaría revisando
                        la probabilidad de que se suba medio grado con la acción "encender" en la
                        temperatura de 18 grados centígrados.

        """

        for accion in self.acciones:
            self.probabilidades[accion] = {}
            for i in range(16, 26):
                self.probabilidades[accion][i] = []

    def comprobar_parametros(self) -> bool:
        """Función que comprueba que los parámetros de la istancia se hayan puesto correctamente."""

        if len(self.costes) == len(self.acciones) and len(self.acciones) > 0:
            for coste in self.costes:
                if coste < 0:
                    return False
            return True

        return False

    def add_probabilidad(self, accion: str, estado: int, efecto: str, valor: int) -> bool:
        """
            Función que añade una probabilidad al termostato de cambiar de estado.
            Se utiliza la organización mencionada anteriormente para añadir la probabilidad.
            Los valores se tratan como enteros, asumiendo que son sobre 100.
        """
        efectos = ["+0.5", "+1", "-0.5", "-1"]

        if accion not in self.acciones or estado not in range(16,26) or efecto not in efectos\
                or valor not in range(0,101):
            return False

        self.probabilidades[accion][estado][efectos.index(efecto)] = valor
        return True

    @property
    def temp_usuario(self):
        """Getter para el atributo temp_usuario."""
        return self.temp_usuario

    @temp_usuario.setter
    def temp_usuario(self, valor):
        """Setter para el atributo temp_usuario."""
        if valor in range(16, 26):
            return valor
        raise ValueError("El valor no está en el rango de 16 a 25 grados!!!")


a = Termostato(20, ["encender", "apagar"], [1, 1])
a.inicializar_probabilidades()
print(a.probabilidades)
