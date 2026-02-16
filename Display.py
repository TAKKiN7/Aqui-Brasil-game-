import machine
from machine import Pin, I2C
from time import sleep as pause
from _thread import start_new_thread as secundario

class Display:
    I2C_ADDR = 0x27
    i2c: I2C = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    BACKLIGHT = 0x08

    def __init__(self):
        self.backlight_state = self.BACKLIGHT
        self._parar = 0
        self.iniciar()
        
    
    @property
    def parar(self):
        return self._parar
    
    @parar.setter
    def parar(self, value):
        self._parar = value
    
    
    def comando(self, cmd, mode=0):
        high = cmd & 0xF0
        low = (cmd << 4) & 0xF0
        for val in (high, low):
            self.i2c.writeto(self.I2C_ADDR, bytes([val | self.backlight_state | 0x04 | mode]))  # EN=1
            pause(0.001)
            self.i2c.writeto(self.I2C_ADDR, bytes([val | self.backlight_state | mode]))  # EN=0

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

    def backlight(self, value: bool = True):
        if not value:
            self.backlight_state = 0x00
            self.comando(0x00)
        else:
            self.backlight_state = self.BACKLIGHT
            self.comando(0x00)

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

    def tarefa(self):
        self._parar = 0
        cont = 1
        while self._parar == 0:
            if cont == 15:
                break
            print(cont)
            cont += 1
            pause(1)
        if self._parar == 1:
            return
        self.backlight(False)


    def desligar_backlight(self):
        secundario(self.tarefa, ())
