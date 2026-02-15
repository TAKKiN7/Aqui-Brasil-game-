import machine
from machine import Pin, I2C
from time import sleep as pause


class Display:
    I2C_ADDR = 0x27
    i2c: I2C = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    BACKLIGHT = 0x08

    def __init__(self):
        self.iniciar()

    def comando(self, cmd, mode=0):
        high = cmd & 0xF0
        low = (cmd << 4) & 0xF0
        for val in (high, low):
            self.i2c.writeto(self.I2C_ADDR, bytes([val | self.BACKLIGHT | 0x04 | mode]))  # EN=1
            pause(0.001)
            self.i2c.writeto(self.I2C_ADDR, bytes([val | self.BACKLIGHT | mode]))  # EN=0

    def iniciar(self):
        pause(0.02)
        self.comando(0x33)
        self.comando(0x32)
        self.comando(0x28)
        pause(.5)
        self.comando(0x0C)
        self.comando(0x06)
        self.limpar()

    def limpar(self):
        self.comando(0x01)
        pause(0.2)

    def linha(self, linha: int = 1):
        if linha == 1:
            self.comando(0x80)  # Primeira linha
        else:
            self.comando(0xC0)  # Segunda linha

    def printar(self, msg):
        for ch in msg:
            self.comando(ord(ch), 1)

    def escrever(self, msg_1: str = "", msg_2: str = "", pulsar: bool = False):
        self.limpar()
        if pulsar:
            for c in range(5):
                self.linha(1)
                self.printar(msg_1)
                self.linha(2)
                self.printar(msg_2)
                pause(.5)
                self.limpar()
            self.limpar()
        else:
            self.linha(1)
            self.printar(msg_1)
            self.linha(2)
            self.printar(msg_2)
