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
    
    
    
def led_iniciar():
    pause(1.2)
    led_g = Pin(2, Pin.OUT)
    led_r = Pin(5, Pin.OUT)
    for c in range(3):
        led_g.on()
        led_r.on()
        pause(0.2)
        led_g.off()
        led_r.off()
        pause(0.2)
        

def led_confirmar():
    led = Pin(2, Pin.OUT)
    for c in range(2):
        led.on()
        pause(0.2)
        led.off()
        pause(0.2)
        
        
def led_error():
    led = Pin(5, Pin.OUT)
    for c in range(2):
        led.on()
        pause(0.2)
        led.off()
        pause(0.2)