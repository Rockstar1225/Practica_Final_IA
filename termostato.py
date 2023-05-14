"""
    Este es el módulo que representa el termostato y su comportamiento en la práctica.
"""
import random


class Termostato:
    """ Clase que representa el objeto termostato y su funcionamiento."""

    def __init__(self, input_temperatura: float, acciones: list, costes: list, estados: list):
        self.__temp_usuario = input_temperatura
        self.acciones = acciones
        self.costes = costes
        self.estados = estados
        self.temp_real = random.choice(self.estados)
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
                        + Mantener la temperatura: indice 3.

                - Ejemplo:
                    Con la consulta "self.probabilidades["encender"][18][0]" se estaría revisando
                        la probabilidad de que se suba medio grado con la acción "encender" en la
                        temperatura de 18 grados centígrados.

        """

        for accion in self.acciones:
            self.probabilidades[accion] = {}
            for i in self.estados:
                self.probabilidades[accion][str(i)] = [0, 0, 0, 0]

    def comprobar_parametros(self) -> bool:
        """Función que comprueba que los parámetros de la istancia se hayan puesto correctamente."""

        if len(self.costes) == len(self.acciones) and len(self.acciones) > 0:
            for coste in self.costes:
                if coste < 0:
                    return False
            return True

        return False

    def add_probabilidad(self, accion: str, estado: int | float, efecto: str, valor: int) -> bool:
        """
            Función que añade una probabilidad al termostato de cambiar de estado.
            Se utiliza la organización mencionada anteriormente para añadir la probabilidad.
            Los valores se tratan como enteros, asumiendo que son sobre 100.
        """
        efectos = ["0.5", "1", "-0.5", "0"]

        if (accion not in self.acciones) or (int(estado) not in self.estados) or (efecto not in efectos) \
                or (valor not in range(101)):
            return False
        self.probabilidades[accion][str(estado)][efectos.index(efecto)] = valor

        return True

    def calcular_camino_optimo(self):
        """
            Función que simula un recorrido por los estados hasta llegar al deseado.
            Retorna el indice de las acciones que se han realizado de acuerdo a una política óptima.
        """
        acciones_optimas = self.encontrar_politica_optima()[0]
        acciones_camino = []
        estado_actual = self.temp_real
        iteracion = 0
        while estado_actual != self.temp_usuario and iteracion < 900:
            iteracion += 1
            accion = acciones_optimas[self.estados.index(int(estado_actual))]
            probabilidades = self.probabilidades[self.acciones[int(accion)]][str(int(estado_actual))]
            list_probs = []


            for i in range(4):
                list_probs += [i for j in range(probabilidades[i])]

            #print(list_probs,len(list_probs),probabilidades)
            indice = random.choice(list_probs)
            if indice == 0:
                estado_actual += 0.5
            elif indice == 1:
                estado_actual += 1
            elif indice == 2:
                estado_actual -= 0.5
            elif indice == 3:
                estado_actual -= 0

            acciones_camino.append(int(accion))

        return acciones_camino

    def encontrar_politica_optima(self) -> tuple:
        """
        Función que implementa el algoritmo de iteración por valor para cada estado del problema.
        Para comprender el algoritmo, es necesario explicar el significado de las variables:
            - valores_anteriores: lista de cardinalidad el número de estados. Ésta almacena los
                valores recogidos anteriormente por los estados en iteraciones anteriores. Por
                defecto, se inicializan todos a 0.

            - valores_nuevos: es la lista donde se guardarán todos los valores de los estados
                óptimos cuando el algoritmo acabe. También tiene como cardinalidad el número
                de estados. Al principio del algoritmo la inicializamos como vacía.

            - acciones_optimas: variable donde se almacenarán los indices de las acciones óptimas
                para cada estado.También tiene como cardinalidad el número de estados.
                Al principio del algoritmo la inicializamos como vacía.

            - fin: variable que indica el momento en el que el algoritmo para de hacer iteraciones.
                Por defecto se inicializa como 0.

            - iteración: variable para llevar una cuenta de las iteraciones producidas.
        """
        valores_anteriores = [0 for i in range(len(self.estados))]
        valores_nuevos = []
        acciones_optimas = []
        iteracion = 0
        fin = False

        # bucle principal de iteración del algoritmo.
        # objetivo: calcular los valores de los estados.
        while not fin:
            iteracion += 1
            valores_nuevos_temp = []
            for estado in self.estados:
                valores_nuevos_temp.append(
                    self.calcular_valor_de_estado(estado, valores_anteriores)
                )

            if valores_nuevos_temp == valores_anteriores:
                valores_nuevos = valores_nuevos_temp
                fin = True
            else:
                valores_anteriores = valores_nuevos_temp

        # Tras haber calculado los valores, se revelan las acciones óptimas.
        for estado in self.estados:
            acciones_optimas.append(
                self.calcular_accion_optima(estado, valores_nuevos)
            )

        return acciones_optimas, valores_nuevos

    def calcular_accion_optima(self, estado: float, valores_actuales: list) -> int:
        """Esta función determina la acción óptima de cada estado.
            :param estado: estado sobre el que calcular sus acciones óptimas.
            :param valores_actuales: los valores actuales de cada estado.
            :return: indice de la acción más óptima para el estado actual.
        """
        if estado not in self.estados:
            raise ValueError("Estado no válido para calcular su valor!!!")

        resultado = []
        for action in self.acciones:
            resultado.append(self.__calcular_formula_bellman(estado, action, valores_actuales))

        return resultado.index(min(resultado))

    def calcular_valor_de_estado(self, estado: float, valores_anteriores: list) -> float:
        """Calcula el valor de un estado basandose en la formula de bellman."""
        if estado not in self.estados:
            raise ValueError("Estado no válido para calcular su valor!!!")

        resultado = []
        for action in self.acciones:
            resultado.append(self.__calcular_formula_bellman(estado, action, valores_anteriores))

        return min(resultado)

    def __calcular_formula_bellman(self, estado: float, action: str,
                                   valores_anteriores: list) -> float:
        """Esta función aplica la formula de Bellman a un estado en específico."""
        result = 0
        if estado != self.temp_real:
            result += self.costes[self.acciones.index(action)]
            for prob in self.probabilidades[action][str(estado)]:
                if self.probabilidades[action][str(estado)].index(prob) == 0:
                    result += prob / 100 * valores_anteriores[self.estados.index(estado + 0.5)] if estado != 25 else 0
                elif self.probabilidades[action][str(estado)].index(prob) == 1:
                    result += prob / 100 * valores_anteriores[self.estados.index(estado + 1)] if estado < 24.5 else 0
                elif self.probabilidades[action][str(estado)].index(prob) == 2:
                    result += prob / 100 * valores_anteriores[self.estados.index(estado - 0.5)] if estado != 16 else 0
                else:
                    result += prob / 100 * valores_anteriores[self.estados.index(estado)]

        return result

    @property
    def temp_usuario(self):
        """Getter para el atributo temp_usuario."""
        return self.__temp_usuario

    @temp_usuario.setter
    def temp_usuario(self, valor):
        """Setter para el atributo temp_usuario."""
        if valor in range(16, 26):
            return valor
        raise ValueError("El valor no está en el rango de 16 a 25 grados!!!")
