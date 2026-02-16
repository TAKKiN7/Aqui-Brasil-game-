from Display import Display
from machine import Pin, I2C
from time import sleep as pause
from pn532 import PN532_I2C
from Leitor import Leitor
from Database import Database
from Banco import Banco
from Cantor import Cantor
from basic_functions import inicializar, led_iniciar
from Teclado import Teclado
from Menu import Menu
from _thread import start_new_thread as secundario

cantor: Cantor = Cantor()
teclado: Teclado = Teclado(cantor)
display: Display = Display()
leitor: Leitor = Leitor(display, cantor)
db: Database = Database()
dados = db.get()
banco: Banco = Banco(db, display, leitor, cantor)
menu: Menu = Menu(teclado, display, banco, dados, leitor)


secundario(led_iniciar, ())
inicializar(display, cantor)  # funçao beep inicializando a maquininha

while True:
    menu.menu()
