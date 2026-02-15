from machine import Pin
from time import sleep as pause
from Cantor import Cantor


class Teclado:
    def __init__(self, cantor: Cantor):
        self.cantor: Cantor = cantor
        self.pinos_linhas = (13, 12, 11, 10)
        self.pinos_colunas = (9, 8, 7, 6)
        self.init()

    def init(self):
        self.linhas = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in self.pinos_linhas]
        self.colunas = [Pin(pin, Pin.OUT) for pin in self.pinos_colunas]

        self.teclas = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"]
        ]

        for c in self.colunas:
            c.value(1)

    def test(self):
        for i, l in enumerate(self.linhas):
            print(i, l.value())
            pause(1)

    def get_teclas(self):
        for c in range(0, 4):
            self.colunas[c].value(0)
            for l in range(0, 4):
                if self.linhas[l].value() == 0:
                    tecla = self.teclas[l][c]

                    while self.linhas[l].value() == 0:
                        pause(0.02)

                    self.colunas[c].value(1)
                    self.cantor.tocar("tecla")
                    return tecla

            self.colunas[c].value(1)
        return None
