from Display import Display
from machine import Pin, I2C
from time import sleep as pause
from pn532 import PN532_I2C
from Leitor import Leitor
from Database import Database
from Banco import Banco
from Cantor import Cantor


def inicializar(display: Display, cantor: Cantor):
    display.escrever("Iniciando", "Aguarde...")
    pause(1)
    cantor.tocar("ligando")