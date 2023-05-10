import os
import unittest
import platform

from csv_loader import CSVloader
from termostato import Termostato


class Pruebas(unittest.TestCase):

    def setUp(self) -> None:
        self.estados = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
        self.acciones = ["encender", "apagar"]

    def test_termostato_1(self):

        termostato = Termostato(22, self.acciones, [100, 1], self.estados)
        loader = CSVloader(self.estados)
        prev = "/" if platform.system() == "Linux" else "\\"

        for file in os.listdir(os.getcwd() + prev + "Probabilidades Condicionales"):

            loader.load_csv(prev + "Probabilidades Condicionales"+ prev + file)
            print(loader.contenido)
            for i in self.estados:
                if i == 16:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 25:
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 24.5:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                else:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
            loader.contenido = []

        print(termostato.probabilidades)
        print("Temperatura ingresada: ",termostato.temp_usuario)
        print("Temperatura real: ",termostato.temp_real)
        print("Costes de Estados Optimos: ",termostato.encontrar_politica_optima()[1])
        print("Acciones Optimas: ",termostato.encontrar_politica_optima()[0])
        camino = termostato.calcular_camino_optimo()
        print("Camino Optimo: ",camino)
        calculo = [self.acciones[i] for i in camino]
        result = []

        return self.assertEqual(result,calculo, "Los caminos no son iguales!!!")

    def test_termostato_2(self):

        termostato = Termostato(22, self.acciones, [1, 100], self.estados)
        loader = CSVloader(self.estados)
        prev = "/" if platform.system() == "Linux" else "\\"

        for file in os.listdir(os.getcwd() + prev + "Probabilidades Condicionales"):

            loader.load_csv(prev + "Probabilidades Condicionales"+ prev + file)
            print(loader.contenido)
            for i in self.estados:
                if i == 16:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 25:
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 24.5:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                else:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
            loader.contenido = []

        print(termostato.probabilidades)
        print("Temperatura ingresada: ", termostato.temp_usuario)
        print("Temperatura real: ", termostato.temp_real)
        print("Costes de Estados Optimos: ", termostato.encontrar_politica_optima()[1])
        print("Acciones Optimas: ", termostato.encontrar_politica_optima()[0])
        camino = termostato.calcular_camino_optimo()
        print("Camino Optimo: ", camino)
        calculo = [self.acciones[i] for i in camino]
        result = []

        return self.assertEqual(result,calculo, "Los caminos no son iguales!!!")

    def test_termostato_3(self):

        termostato = Termostato(22, self.acciones, [10, 10], self.estados)
        loader = CSVloader(self.estados)
        prev = "/" if platform.system() == "Linux" else "\\"

        for file in os.listdir(os.getcwd() + prev + "Probabilidades Condicionales"):

            loader.load_csv(prev + "Probabilidades Condicionales"+ prev + file)
            print(loader.contenido)
            for i in self.estados:
                if i == 16:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 25:
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 24.5:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                else:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
            loader.contenido = []

        print(termostato.probabilidades)
        print("Temperatura ingresada: ", termostato.temp_usuario)
        print("Temperatura real: ", termostato.temp_real)
        print("Costes de Estados Optimos: ", termostato.encontrar_politica_optima()[1])
        print("Acciones Optimas: ", termostato.encontrar_politica_optima()[0])
        camino = termostato.calcular_camino_optimo()
        print("Camino Optimo: ", camino)
        calculo = [self.acciones[i] for i in camino]
        result = []

        return self.assertEqual(result,calculo, "Los caminos no son iguales!!!")

    def test_termostato_4(self):

        termostato = Termostato(22, self.acciones, [6,5], self.estados)
        loader = CSVloader(self.estados)
        prev = "/" if platform.system() == "Linux" else "\\"

        for file in os.listdir(os.getcwd() + prev + "Probabilidades Condicionales"):

            loader.load_csv(prev + "Probabilidades Condicionales"+ prev + file)
            print(loader.contenido)
            for i in self.estados:
                if i == 16:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 25:
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 24.5:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                else:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
            loader.contenido = []

        print(termostato.probabilidades)
        print("Temperatura ingresada: ", termostato.temp_usuario)
        print("Temperatura real: ", termostato.temp_real)
        print("Costes de Estados Optimos: ", termostato.encontrar_politica_optima()[1])
        print("Acciones Optimas: ", termostato.encontrar_politica_optima()[0])
        camino = termostato.calcular_camino_optimo()
        print("Camino Optimo: ", camino)
        calculo = [self.acciones[i] for i in camino]
        result = []

        return self.assertEqual(result,calculo, "Los caminos no son iguales!!!")

    def test_termostato_5(self):

        termostato = Termostato(22, self.acciones, [5,6], self.estados)
        loader = CSVloader(self.estados)
        prev = "/" if platform.system() == "Linux" else "\\"

        for file in os.listdir(os.getcwd() + prev + "Probabilidades Condicionales"):

            loader.load_csv(prev + "Probabilidades Condicionales"+ prev + file)
            print(loader.contenido)
            for i in self.estados:
                if i == 16:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 25:
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 24.5:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                else:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5",
                                                loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
            loader.contenido = []

        print(termostato.probabilidades)
        print("Temperatura ingresada: ", termostato.temp_usuario)
        print("Temperatura real: ", termostato.temp_real)
        print("Costes de Estados Optimos: ", termostato.encontrar_politica_optima()[1])
        print("Acciones Optimas: ", termostato.encontrar_politica_optima()[0])
        camino = termostato.calcular_camino_optimo()
        print("Camino Optimo: ", camino)
        calculo = [self.acciones[i] for i in camino]
        result = []

        return self.assertEqual(result,calculo, "Los caminos no son iguales!!!")
