import os
import unittest

from csv_loader import CSVloader
from termostato import Termostato


class Pruebas(unittest.TestCase):
    @staticmethod
    def setUpClass() -> None:
        pass

    def setUp(self) -> None:
        pass

    def test_termostato_1(self):
        estados = [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]
        acciones = ["encender", "apagar"]

        termostato = Termostato(22, acciones,[0, 0],estados)
        loader = CSVloader(estados)
        for file in os.listdir(os.getcwd()+"\\Probabilidades Condicionales"):

            loader.load_csv("\\Probabilidades Condicionales\\"+file)

            for i in estados:
                if 16 < i < 24.5:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i,i+0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5", loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 16:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "1", loader.localizar_probabilidad(i, i + 1))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 25:
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5", loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))
                elif i == 24.5:
                    termostato.add_probabilidad(file.strip(".csv"), i, "0.5", loader.localizar_probabilidad(i, i + 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "-0.5", loader.localizar_probabilidad(i, i - 0.5))
                    termostato.add_probabilidad(file.strip(".csv"), i, "0", loader.localizar_probabilidad(i, i))

        print(termostato.probabilidades)
        result = []

        return self.assertEqual(termostato.calcular_camino_optimo(),result,"Los caminos no son iguales!!!")
