import unittest
from termostato import Termostato
class Pruebas(unittest.TestCase):
    def setUpClass(cls) -> None:

        termostato = Termostato(input_temperatura= 22, acciones= ["encender", "apagar"], costes= [0, 0],
                                estados=[16, 16.5, 17, 17.5, 18, 18.5, 19,
                                         19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25])
    def setUp(self) -> None:
        pass
